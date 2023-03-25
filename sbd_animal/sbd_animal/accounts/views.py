import datetime
from django.contrib.auth import get_user_model, authenticate
from django.middleware import csrf
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, generics, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

import random

from .serializers import SignUpSerializers, ProfileSerializer, ProfileEditSerializer
from .task import test_email, send_verification_email


# Create your views here.


class SignUpView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = SignUpSerializers
    permission_classes = [permissions.AllowAny]


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def send_signup_verification_code(req):
    ini_verification_code = random.randint(
        10000000, 99999999
    )  # generate number between 100000 ~ 999999
    verification_code = (ini_verification_code * 2) + 1234
    # TODO: send email to user with verification code.
    email_address = req.GET.get("email_address", "")
    user_name = req.GET.get("username", "")
    User = get_user_model()
    users = User.objects.all()
    # 만약 email이나 username 사용중이면 반환처리
    if users:
        for user in users:
            if user.email == email_address:
                return Response(
                    {"error_cause": "email"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif user.username == user_name:
                return Response(
                    {"error_cause": "username"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    send_verification_email.delay(email_address, user_name, verification_code)
    return Response({"verification_code": verification_code}, status=status.HTTP_200_OK)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        """
        django.auth.login 사용하지 못하므로 last_login 수동으로 업데이트 진행한다.
        """
        data = request.data
        response = Response()
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"],
                    value=data["access"],
                    expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=True,
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                )
                response.set_cookie(
                    key=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
                    value=data["refresh"],
                    expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully", "data": data}
                user.last_login = datetime.datetime.now()
                user.save()
                return response
            else:
                return Response(
                    {"No active": "This account is not active!!"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"Invalid": "Invalid username or password!!"},
                status=status.HTTP_404_NOT_FOUND,
            )


@api_view(["GET"])
def logout(req):
    """
    authenticated 된 user의 모든 토큰을 삭제해준다.
    """
    res = Response()
    res.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"], samesite="None")
    res.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"], samesite="None")
    res.delete_cookie("csrftoken")
    return res


@api_view(["GET"])
@authentication_classes(
    []
)  # access_token이 만료되어도 접근할 수 있어야 하므로 authentication을 진행하지 않는다.
@permission_classes([permissions.AllowAny])
def test_access_code(req):
    raw_refresh_token = req.COOKIES.get(
        settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"], None
    )
    raw_access_token = req.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"], None)
    # TODO: 토큰 claim["user_id"]로 접근 하는 것과 req.user.id로 접근 하는 값이 같은지 확인하기
    # TODO: raw_refresh_token이 None인 경우 login시키기
    if raw_refresh_token is None:
        # 활성화된 token이 없으면 보내는 응답
        return Response({"message": "no tokens"})
    try:
        validated_refresh_token = RefreshToken(raw_refresh_token)
        try:
            # refresh token, access token 모두 유효한 경우 이므로 그대로 반환
            validated_access_token = AccessToken(raw_access_token)
            return Response(
                {"message": "all tokens are valid"},
                status=status.HTTP_200_OK,
            )
        except TokenError as e:
            # refresh token이 유효하지만 access code가 만료되었을때 access_code 재발급
            new_access_token = validated_refresh_token.access_token
            res = Response({"message": "new access code created"})
            res.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"],
                value=new_access_token,
                expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                httponly=False,
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
            )
            return res
    except TokenError as e:
        # refresh token이 존재하나 만료 되었으므로 cookie에서 제거한 후 login url로 redirect
        res = Response({"message": "refresh token is expired"})
        res.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_ACCESS"])
        res.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"])
        res.delete_cookie("csrftoken")
        return res


@api_view(["GET", "PUT"])
@permission_classes([permissions.IsAuthenticated])
def user_profile(req):
    if req.method == "GET":
        serializer = ProfileSerializer(req.user)
        return Response({"user": serializer.data})
    if req.method == "PUT":
        serializer = ProfileEditSerializer(req.user, data=req.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
