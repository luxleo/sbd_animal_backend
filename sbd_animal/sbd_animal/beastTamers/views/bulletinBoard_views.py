from django.shortcuts import get_object_or_404
from django.db.models import ProtectedError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from sbd_animal.bulletinBoard.models import Inquery, Reply
from sbd_animal.bulletinBoard.serializers import (
    InqueryListSerializer,
    ReplySerializer,
    InqueryDetailSerializer,
)


@api_view(["GET"])
@authentication_classes([SessionAuthentication])
def inquery_list(req):
    qs = Inquery.objects.select_related("author").all()
    serializer = InqueryListSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([SessionAuthentication])
def inquery_detail(req, pk):
    try:
        inquery = (
            Inquery.objects.select_related("author")
            .prefetch_related("reply_set")
            .get(pk=pk)
        )
        reply_set = inquery.reply_set.select_related("author").all()
        inquery_serializer = InqueryDetailSerializer(inquery)
        reply_serializer = ReplySerializer(reply_set, many=True)
        return Response(
            {"inquery": inquery_serializer.data, "reply_list": reply_serializer.data}
        )
    except ObjectDoesNotExist:
        return Response(
            {"message": "no such inquery"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST", "PUT", "DELETE"])
@authentication_classes([SessionAuthentication])
def reply_view(req):
    if req.method == "POST":
        serializer = ReplySerializer(data={"content": req.data.get("content", None)})
        if serializer.is_valid():
            # inquery에 댓글이 추가 되었으므로 상태 값을 '응답'으로 바꾸고 생성된 댓글 저장
            inquery = get_object_or_404(Inquery, pk=req.data.get("inquery_pk", None))
            inquery.state = "Y"
            inquery.save()
            serializer.save(author=req.user, inquery=inquery)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == "PUT":
        target_id = req.data.get("reply_id", None)
        obj = get_object_or_404(Reply, id=target_id)
        update_data = {"content": req.data.get("content", None)}
        serializer = ReplySerializer(obj, data=update_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        obj = get_object_or_404(Reply, id=req.data.get("reply_id", None))
        try:
            obj.delete()
            return Response({"message": "success fully deleted"})
        except ProtectedError:
            message = "this reply cannot be deleted"
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
