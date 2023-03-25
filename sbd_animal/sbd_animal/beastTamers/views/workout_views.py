from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from sbd_animal.work_out.serializers import WorkoutTypeSerializer
from sbd_animal.work_out.models import WorkoutType


@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication])
def workout_types(req):
    if req.method == "GET":
        qs = WorkoutType.objects.all()
        serializer = WorkoutTypeSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == "POST":
        serializer = WorkoutTypeSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
@authentication_classes([SessionAuthentication])
def workout_type(req, pk):
    if req.method == "PUT":
        obj = get_object_or_404(WorkoutType, pk=pk)
        serializer = WorkoutTypeSerializer(obj, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            {"message": "something wrong with request"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    elif req.method == "DELETE":
        obj = get_object_or_404(WorkoutType, pk=pk)
        try:
            obj.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(
                {"message": "something wrong with delete"},
                status=status.HTTP_400_BAD_REQUEST,
            )
