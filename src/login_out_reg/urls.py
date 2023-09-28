"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from login_out_reg.views import registration, log_in, log_out, \
    profile, add_profile_data, edit_profile, delete_user, detail_past_order

urlpatterns = [

    path("registration", registration, name="registration"),
    path("login", log_in, name="log_in"),
    path("logout", log_out, name="log_out"),
    path("profile", profile, name="profile"),
    path("add_profile_data", add_profile_data, name="add_profile_data"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("delete_user", delete_user, name="delete_user"),
    path("detail_past_order", detail_past_order, name="detail_past_order"),
    path('reset_password/', PasswordResetView.as_view(template_name="reset_password.html"), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name='password_reset_confirm'),
        path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete')
]
