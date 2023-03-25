from django.contrib import admin

from .models import WorkoutType, Log


# Register your models here.


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "workout_distance", "id"]


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["athlete", "id", "workout_type", "created_at"]
