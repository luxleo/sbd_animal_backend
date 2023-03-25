from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        instance.is_active = validated_data.get("is_active")
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "date_joined",
            "last_login",
            "is_active",
        ]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "date_joined",
            "last_login",
            "is_active",
        ]
