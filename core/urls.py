from django.urls import path
from .views import home, signup, login_view, logout, settings

app_name = "core"

urlpatterns = [
    path("", home, name="home_view"),
    path("settings/", settings, name="settings"),
    path("signup/", signup, name="signup_view"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout, name="logout_view"),
]
