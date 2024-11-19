from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def home(request):
    title = "SSC SocialMedia"
    context = {"title": title}
    return render(request, "index.html", context)


def signup(request):
    title = "SSC Sign Up"

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "E-Mail Adresse existiert bereits")
                return redirect("core:signup_view")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Benutzername existiert bereits")
                return redirect("core:signup_view")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                messages.success(request, "Account wurde erfolgreich angelegt")
                return redirect("core:signup_view")
        else:
            messages.error(request, "Passwörter stimmen nicht überein")
            return redirect("core:signup_view")

    context = {"title": title}
    return render(request, "signup.html", context)
