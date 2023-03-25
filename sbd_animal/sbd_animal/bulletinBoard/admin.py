from django.contrib import admin
from .models import Inquery, Reply

# Register your models here.


@admin.register(Inquery)
class InqueryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "inquery", "content", "created_at"]
