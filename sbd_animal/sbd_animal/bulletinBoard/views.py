from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Inquery, Reply
from .serializers import (
    InqueryDetailSerializer,
    InqueryListSerializer,
    ReplySerializer,
)

# Create your views here.


@api_view(["GET", "POST", "DELETE"])
def user_inquery_view(req):
    if req.method == "GET":
        qs = Inquery.objects.filter(author=req.user).select_related("author")
        serializer = InqueryListSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == "POST":
        new_inquery = Inquery(
            author=req.user,
            title=req.data.get("title"),
            content=req.data.get("content"),
            state="N",
        )
        new_inquery.save()
        return Response(status=status.HTTP_201_CREATED)
    elif req.method == "DELETE":
        target_ids = req.data.get("delete_id_list")
        qs = Inquery.objects.filter(pk__in=target_ids, author=req.user)
        for inquery in qs:
            inquery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT"])
def user_inquery_detail_view(req, pk):
    if req.method == "GET":
        inquery = (
            Inquery.objects.filter(id=pk)
            .select_related("author")
            .prefetch_related("reply_set")
            .first()
        )
        if req.user == inquery.author:
            serializer = InqueryDetailSerializer(inquery)
            # reply의 author를 불러 오기위해 select_related함수로 INNER JOIN 처리
            replies = inquery.reply_set.select_related("author").all()
            reply_list = []
            for reply in replies:
                reply_list.append(ReplySerializer(reply).data)
            res = {"inquery": serializer.data, "reply_list": reply_list}
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    if req.method == "PUT":
        target_inquery = get_object_or_404(Inquery, pk=pk, author=req.user)
        serializer = InqueryDetailSerializer(
            target_inquery, data=req.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST", "PUT", "DELETE"])
def post_inquery_reply(req):
    # 유저가 의문에 대한 덧글을 달면 inquery의 상태를 P(추가 답변)으로 바꾼다.
    if req.method == "POST":
        reply_inquery_id = req.data.get("inquery_id", None)
        reply_content = req.data.get("content", None)
        if reply_content is None or reply_inquery_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        target_inquery = get_object_or_404(Inquery, id=reply_inquery_id)
        target_inquery.state = "P"
        new_reply = Reply(
            author=req.user, inquery=target_inquery, content=reply_content
        )
        new_reply.save()
        target_inquery.save()
        serializer = ReplySerializer(new_reply)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif req.method == "PUT":
        target_reply = get_object_or_404(Reply, id=req.data.get("id"))
        serializer = ReplySerializer(target_reply, data=req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method == "DELETE":
        Reply.objects.filter(id=req.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
