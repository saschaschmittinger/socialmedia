from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


@login_required
def home(request):
    title: str = "SSC SocialMedia"
    template: str = "index.html"
    context: dict = {"title": title}
    return render(request, template, context)


@login_required
def settings(request):
    title: str = "SSC Settings"
    template: str = "setting.html"

    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        if request.FILES.get("image") == None:
            image = user_profile.profile_img
            bio = request.POST["bio"]
            location = request.POST["location"]

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            messages.success(request, "Daten wurden erfolgreich gespeichert")

        if request.FILES.get("image") != None:
            image = request.FILES.get("image")
            bio = request.POST["bio"]
            location = request.POST["location"]

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            messages.success(request, "Daten wurden erfolgreich gespeichert")
        return redirect("core:settings")

    context: dict = {"title": title, "user_profile": user_profile}
    return render(request, template, context)


def signup(request):
    title: str = "SSC Sign Up"
    template: str = "signup.html"

    if request.user.is_authenticated:
        messages.info(request, "Sie sind bereits registriert.")
        return redirect("core:home_view")

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
                # Login and redirect to settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                messages.success(request, "Account wurde erfolgreich angelegt")

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("core:settings")

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

    if request.user.is_authenticated:
        messages.info(request, "Sie sind bereits angemeldet.")
        return redirect("core:home_view")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Sie wurden erfolgreich angemeldet")
            return redirect("core:home_view")
        else:
            messages.error(request, "bitte überprüfen Sie Benutzername und Passwort")

    context: dict = {"title": title}
    return render(request, template, context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Sie wurden erfolgreich abgemeldet")
    return redirect("core:login_view")
