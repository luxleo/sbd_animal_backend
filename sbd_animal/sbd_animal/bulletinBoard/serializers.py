from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Inquery, Reply


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "avatar_url"]


class InqueryListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Inquery
        fields = ["id", "author", "title", "state_label", "created_at"]


class InqueryDetailSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.content = validated_data.get("content")
        instance.save()
        return instance

    class Meta:
        model = Inquery
        fields = ["id", "title", "content", "state", "created_at"]


class ReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.content = validated_data.get("content")
        instance.save()
        return instance

    class Meta:
        model = Reply
        fields = ["id", "author", "content", "created_at"]


class ReplyPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ["id", "content"]
