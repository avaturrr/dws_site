from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from dws_site.models import Dws


# Create your views here.
def aaa(request):
    if request.method == "GET":
        data = {"dws": Dws.objects.all()}
        return render(request, "index.html", context=data)


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect("aaa")
    #        messages.error(request, form.errors)
    #        redirect("registration")
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {"form": form})


def log_in(request):
    if request.method == "GET":
        form_log = AuthenticationForm()
        return render(request, "login.html", {"form": form_log})
    else:
        form_log = AuthenticationForm(data=request.POST)
        print(f"!!!!!!!!!!!!!!{form_log}!!!!!!!!!!!{form_log.get_user()}")
        if form_log.is_valid():
            login(request, form_log.get_user())
        return redirect("aaa")


def log_out(request):
    logout(request)
    return redirect("aaa")
