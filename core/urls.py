from django.urls import path
from .views import home, signup, login_view

app_name = "core"

urlpatterns = [
    path("", home, name="home_view"),
    path("signup/", signup, name="signup_view"),
    path("login/", login_view, name="login_view"),
]
