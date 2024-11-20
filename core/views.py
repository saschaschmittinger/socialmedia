from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages


def home(request):
    title: str = "SSC SocialMedia"
    template: str = "index.html"
    context: dict = {"title": title}
    return render(request, template, context)


def signup(request):
    title: str = "SSC Sign Up"
    template: str = "signup.html"

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2 and not password == "" and not password2 == "":
            if User.objects.filter(email=email).exists():
                messages.info(request, "E-Mail Adresse existiert bereits")
                return redirect("core:signup_view")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Benutzername existiert bereits")
                return redirect("core:signup_view")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                messages.success(request, "Account wurde erfolgreich angelegt")

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("core:signup_view")

        elif password == "" and password2 == "":
            messages.error(request, "Bitte alle Felder ausfüllen!")

        else:
            messages.error(request, "Passwörter stimmen nicht überein")
            return redirect("core:signup_view")

    context: dict = {"title": title}
    return render(request, template, context)


def login_view(request):
    title: str = "SSC Login"
    template: str = "signin.html"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("core:home_view")
        else:
            messages.error(request, "bitte überprüfen Sie Benutzername und Passwort")

    context: dict = {"title": title}
    return render(request, template, context)
