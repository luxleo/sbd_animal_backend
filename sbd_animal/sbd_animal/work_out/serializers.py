from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import WorkoutType, Log, Rep


class WorkoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutType
        fields = ["id", "name", "workout_distance", "category"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.workout_distance = validated_data.get(
            "workout_distance", instance.workout_distance
        )
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class LogGetSerializer(serializers.ModelSerializer):
    workout_type = WorkoutTypeSerializer(read_only=True)

    class Meta:
        model = Log
        fields = [
            "id",
            "workout_type",
            "max_1rm",
            "total_cal",
            "total_lift",
            "body_weight",
            "percentile",
            "created_at",
            "num_sets",
        ]


class DashBoardLogSerializer(serializers.ModelSerializer):
    workout_type = WorkoutTypeSerializer(read_only=True)

    class Meta:
        model = Log
        fields = [
            "id",
            "workout_type",
            "max_1rm",
            "percentile",
            "body_weight",
            "created_at",
        ]


User = get_user_model()


class UserWeightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["weight"]


class LogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = [
            "workout_type",
            "max_1rm",
            "total_cal",
            "total_lift",
            "body_weight",
            "percentile",
            "num_sets",
        ]


class RepGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = []


class RepPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = ["id", "rep_order_number", "calorie", "workout_weight", "reps"]
