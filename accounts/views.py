from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import auth

class Home(TemplateView):
    template_name = "base.html"

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["confirm"]:
            user = User.objects.create_user(
                email=request.POST["email"],
                username=request.POST["username"],
                password=request.POST["password"],
            )
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("home")
    else:
        return render(request, "accounts/signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            return redirect('home')
        else:
            return render(request, "accounts/login.html", {"error" : "username or password is not correct"})
    else:
        return render(request, "accounts/login.html")