from django.db.models import TextField
from django.db.models.functions import Concat

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import WorkoutType, Log
from .serializers import (
    WorkoutTypeSerializer,
    LogPostSerializer,
    LogGetSerializer,
    RepPostSerializer,
    UserWeightUpdateSerializer,
    DashBoardLogSerializer,
)
from ..accounts.serializers import ProfileSerializer


# Create your views here.


@api_view(["GET"])
def get_workout_types(req):
    qs = WorkoutType.objects.all()
    serializer = WorkoutTypeSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def post_log(req):
    """
    req 요청으로 Log instance 만드는 serializer와
    response로 생성된 Log instance 반환하는 serializer 따로 두었다.(화면단에서 바로 사용할수 있도록)
    :param req:
    :return:
    """
    if req.method == "POST":
        payload_log = req.data.get("logData")
        payload_reps = req.data.get("repData")

        reps_response = []
        log_serializer = LogPostSerializer(data=payload_log)

        if log_serializer.is_valid():
            new_log = log_serializer.save(athlete=req.user)
            # log내에서 user body_weight값이 기존 user weight값과 다를 때 업데이트
            if new_log.body_weight != req.user.weight:
                user = UserWeightUpdateSerializer(
                    req.user, data={"weight": new_log.body_weight}, many=False
                )
                if user.is_valid():
                    user.save()

            res_serializer = LogGetSerializer(new_log, many=False)
            for rep in payload_reps:
                rep_serializer = RepPostSerializer(data=rep)
                if rep_serializer.is_valid():
                    rep_serializer.save(log=new_log)
                    reps_response.append(rep_serializer.data)
            res = Response({"log": res_serializer.data, "reps": reps_response})
            return res
    return Response("something happened")


@api_view(["GET"])
def list_history(req):
    paginator = PageNumberPagination()
    paginator.page_size = 15
    qs = Log.objects.filter(athlete=req.user).select_related("workout_type")
    paginated_qs = paginator.paginate_queryset(qs, req)
    serializer = LogGetSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data)


class LogRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = (
        Log.objects.all().select_related("workout_type").prefetch_related("rep_set")
    )
    serializer_class = LogGetSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        reps = []
        for rep in instance.rep_set.all():
            rep_serializer = RepPostSerializer(rep)
            reps.append(rep_serializer.data)
        return Response({"log": serializer.data, "reps": reps})

    def destroy(self, request, *args, **kwargs):
        """
        only author can delete log
        """
        instance = self.get_object()
        if request.user == instance.athlete:
            self.perform_destroy(instance)
            return Response(
                data={"message": "successfully deleted"},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                data={"message": "you can't destroy other's log"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["GET"])
def graph_log_list(req):
    """
    한 날짜에 같은 운동을 여러번 한 경우 가장 성적이 좋은 운동만 반환한다.
    :return:
    """
    from datetime import datetime, timedelta

    target_workout_name = req.GET.get("target_workout_name", None)
    last_day = req.GET.get("last_day", None)
    scope_range = req.GET.get("scope_range", None)
    date_format = "%Y-%m-%d"
    # default로 10개의 로그 먼저 내보낸다.
    qs = Log.objects.filter(
        workout_type__name__in=[target_workout_name], athlete=req.user
    ).select_related("workout_type")[:10]

    if scope_range == "1":
        last_day = datetime.strptime(last_day, date_format).date()

        qs = Log.objects.filter(
            workout_type__name__in=[target_workout_name],
            athlete=req.user,
            created_at__gte=last_day - timedelta(days=30),
            created_at__lte=last_day - timedelta(days=1),
        ).select_related("workout_type")
    elif scope_range == "3":
        last_day = datetime.strptime(last_day, date_format).date()
        qs = Log.objects.filter(
            workout_type__name__in=[target_workout_name],
            athlete=req.user,
            created_at__gte=last_day - timedelta(days=60),
            created_at__lte=last_day - timedelta(days=1),
        ).select_related("workout_type")
    elif scope_range == "6":
        last_day = datetime.strptime(last_day, date_format).date()
        qs = Log.objects.filter(
            workout_type__name__in=[target_workout_name],
            athlete=req.user,
            created_at__gte=last_day - timedelta(days=90),
            created_at__lte=last_day - timedelta(days=1),
        ).select_related("workout_type")
    elif scope_range == "all":
        qs = Log.objects.filter(
            workout_type__name__in=[target_workout_name],
            athlete=req.user,
        ).select_related("workout_type")

    # squat,bench press ,deadlift의 운동중 같은 날짜에 여러번 운동한 경우를 제외 시킬 필드를 정의 (dist_name)
    dist_qs = qs.annotate(
        dist_name=Concat("workout_type__name", "created_at", output_field=TextField())
    )
    import operator

    # mysql 에서는 distinct on api를 지원 하지 않아서 로직으로 구현
    dist_qs = sorted(
        dist_qs, key=operator.attrgetter("created_at", "percentile"), reverse=True
    )
    res = []
    tmp_unique = []
    for dist in dist_qs:
        if dist.dist_name not in tmp_unique:
            res.append(dist)
            tmp_unique.append(dist.dist_name)

    serializer = DashBoardLogSerializer(res, many=True)
    return Response(serializer.data)
