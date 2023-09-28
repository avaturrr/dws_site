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

from django.urls import path

from login_out_reg.views import registration, log_in, log_out, \
    profile, add_profile_data, edit_profile, delete_user

urlpatterns = [

    path("registration", registration, name="registration"),
    path("login", log_in, name="log_in"),
    path("logout", log_out, name="log_out"),
    path("profile", profile, name="profile"),
    path("add_profile_data", add_profile_data, name="add_profile_data"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("delete_user", delete_user, name="delete_user"),
]
