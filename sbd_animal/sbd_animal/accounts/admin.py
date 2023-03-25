from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "photo"]

    def photo(self, user):
        return mark_safe(f"<img src={user.avatar_url} style='width:48px'/>")
