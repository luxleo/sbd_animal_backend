from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView

from ..serializers.user_serializers import (
    UserSerializer,
    AdminUserSerializer,
    UserDetailSerializer,
)

# Create your views here.

User = get_user_model()


def redirect_view(req):
    """
    /beastTamers/users/*,
    /beastTamers/FAQ/*으로 접근시 템플릿을 반환하는 index URL로 리다이렉트
    """
    return redirect("beastTamers:index_template")


@ensure_csrf_cookie
def set_csrf_token(req):
    return JsonResponse({"message": "CSRF Cookie Set"})


@method_decorator(csrf_protect, name="dispatch")
class CheckAuth(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            is_authenticated = User.is_authenticated
            if is_authenticated:
                return Response(
                    {"message": "authenticated"},
                    status=status.HTTP_200_OK,
                )
            return Response({"message": "not authenticated"}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"message": "something went wrong with check authenticated"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class InitialWhoAmI(APIView):
    """
    페이지 새로고침 등으로 이탈했을때 세션토큰 유효할시 유저 정보 가져옴
    """

    authentication_classes = [SessionAuthentication]

    def get(self, req):
        user = req.user
        serializer = AdminUserSerializer(user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


@method_decorator(csrf_protect, name="dispatch")
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = self.request.data
        email = data.get("email", None)
        password = data.get("password", None)
        try:
            staff_user = authenticate(email=email, password=password)
            if staff_user is not None:
                if staff_user.is_staff:
                    try:
                        login(request, staff_user)
                    except:
                        return Response(
                            {"authentication": "something went wrong with login"}
                        )
                    serializer = AdminUserSerializer(staff_user)
                    return Response(
                        {"message": "staff logged in", "user": serializer.data}
                    )
                return Response({"message": "only admin user can enter"})
        except:
            return Response({"authentication": "authentication wend wrong"})


class LogoutView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request, format=None):
        try:
            logout(request)
            return Response(
                {"message": "staff user logged out"}, status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"message": "something went wrong with logout"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def get_all_users(req):
    qs = User.objects.all()
    serializer = UserSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT"])
@authentication_classes([SessionAuthentication])
@permission_classes([permissions.IsAdminUser])
def user_detail(req, pk):
    if req.method == "GET":
        user = get_object_or_404(User, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == "PUT":
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=req.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message": "wrong request"}, status=status.HTTP_400_BAD_REQUEST
        )
