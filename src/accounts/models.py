from django.db import models
from django.contrib.auth.models import AbstractUser

#abstract user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
#abstract user
# Create your models here.
