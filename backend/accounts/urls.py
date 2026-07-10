from django.urls import path
from accounts.views import register, show_profile

urlpatterns = [
    path("auth/register/", register, name="register"),
    path("auth/profile/", show_profile, name="show_profile"),
]