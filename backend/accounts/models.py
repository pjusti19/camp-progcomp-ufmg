from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    codeforces_handle = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["codeforces_handle"]
    def __str__(self):
        return self.email or self.codeforces_handle


