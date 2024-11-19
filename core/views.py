from django.shortcuts import render


def home(request):
    title = "SSC SocialMedia"
    context = {"title": title}
    return render(request, "index.html", context)


def signup(request):
    title = "SSC Sign Up"
    context = {"title": title}
    return render(request, "signup.html", context)
