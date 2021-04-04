from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

User = get_user_model()

class Home(TemplateView):
    template_name = "base.html"

class SignUp(CreateView):
    model = User
    fields = ["username", "email", "password"]
    template_name = "accounts/signup.html"
    success_url = "/"

class LogIn(LoginView):
    template_name = "accounts/login.html"
    success_url = "/"

def logout(request):
    #remember logout() doesn't throw any errors if the user wasn’t logged in.
    auth.logout(request)
    return redirect("home")