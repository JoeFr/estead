# app_name = 'users'
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url("^accounts/", include("django.contrib.auth.urls")),
    url("^profile/", views.profile, name="user_profile"),
    url("^register/", views.register, name="user_register"),
]
