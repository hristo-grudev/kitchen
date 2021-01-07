from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from main.models import Recipes


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    profile_image = models.ImageField(
        upload_to="profiles/"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
