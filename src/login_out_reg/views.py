from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from login_out_reg.forms import RegisterUserForm

from order.forms import OrderForm

from login_out_reg.models import Profile

from order.models import Order, OrderItem

from login_out_reg.forms import ProfileForm


# Create your views here.


def registration(request):
    if request.method == "POST":
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            #            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect("home_page")
    #        messages.error(request, form.errors)
    #        redirect("registration")
    else:
        form = RegisterUserForm()
    return render(request, "registration.html", {"form": form})


def log_in(request):
    if request.method == "GET":
        form_log = AuthenticationForm()
        return render(request, "login.html", {"form": form_log})
    else:
        form_log = AuthenticationForm(data=request.POST)
        if form_log.is_valid():
            login(request, form_log.get_user())
        return redirect("home_page")


def log_out(request):
    logout(request)
    return redirect("home_page")


def add_profile_data(request):
    if request.method == "GET":
        form_for_profile = ProfileForm(profile=None)
        return render(request, "add_profile_data.html", {"form_for_profile": form_for_profile})
    else:
        used_profil = None
        form_for_profile = ProfileForm(used_profil, request.POST)
        if form_for_profile.is_valid():
            data_for_save = form_for_profile.save(commit=False)
            data_for_save.user = request.user
            data_for_save.save()
        return redirect("profile")


def profile(request):
    if request.method == "GET":
        if Profile.objects.filter(user=request.user).exists():
            profile_data = Profile.objects.get(user=request.user)
            data = {"company_name": profile_data.company_name, "company_tax_id": profile_data.company_tax_id,
                    "legal_adress": profile_data.legal_adress, "post_adress": profile_data.post_adress,
                    "company_email": profile_data.company_email, "phone_number": profile_data.phone_number,
                    "delivery_adress": profile_data.delivery_adress, "position": profile_data.position,
                    "position_name": profile_data.position_name, "bank_details": profile_data.bank_details,
                    "profile_exist": "1"}
        else:
            data = {"profile_exist": "0"}
        return render(request, "profile.html", context=data)


def edit_profile(request):
    used_profile = Profile.objects.get(user=request.user)
    if request.method == "GET":
        form_for_profile = ProfileForm(used_profile)
        return render(request, "edit_profile_data.html", {"form_for_profile": form_for_profile})
    else:
        form_for_profile = ProfileForm(used_profile, request.POST, instance=used_profile)
        if form_for_profile.is_valid():
            form_for_profile.save()
        return redirect("profile")


def delete_user(request):
    user_for_delete = request.user
    user_for_delete.delete()
    return redirect("home_page")
