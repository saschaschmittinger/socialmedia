from django.contrib import admin
from .models import Profile, Post, LikePost


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display: list = ["user", "bio", "location"]
    list_filter: list = ["user", "id_user", "location"]
    fields: list = ["user", "id_user", "bio", "profile_img", "location"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display: list = ["user", "id", "created_at"]
    list_filter: list = ["user", "capton", "created_at", "updated_at", "no_of_likes"]
    fields: list = [
        "id",
        "user",
        "image",
        "capton",
        "no_of_likes",
        "created_at",
        "updated_at",
    ]
    readonly_fields: list = ["created_at", "updated_at"]


@admin.register(LikePost)
class LikeAdmin(admin.ModelAdmin):
    list_display: list = ["username", "post_id"]
    list_filter: list = ["username", "post_id"]
    fields: list = ["post_id", "username"]
    readonly_fields: list = ["post_id"]
