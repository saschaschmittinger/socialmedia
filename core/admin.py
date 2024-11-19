from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display: list = ["user", "bio", "location"]
    list_filter: list = ["user", "id_user", "location"]
    fields: list = ["user", "id_user", "bio", "profile_img", "location"]
