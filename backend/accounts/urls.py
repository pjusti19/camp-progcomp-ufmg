from django.urls import path
from accounts.views import register

urlpatterns = [
    path("auth/register/", register, name="register"),
]