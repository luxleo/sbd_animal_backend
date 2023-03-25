from django.contrib.auth import get_user_model
from rest_framework import serializers


import random


User = get_user_model()


class SignUpSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # db에서 읽어올 값이 아니라 쓰기 전용임을 명시

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            height=validated_data["height"],
            weight=validated_data["weight"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "password", "height", "weight", "email", "avatar", "pk"]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "height", "weight", "avatar_url"]


class ProfileEditSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(allow_null=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.height = validated_data.get("height", instance.height)
        instance.weight = validated_data.get("weight", instance.weight)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["username", "height", "weight", "avatar"]
