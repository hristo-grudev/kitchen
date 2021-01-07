from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from main.models import Recipes


class UserOrders(models.Model):
    order_id = models.AutoField(primary_key=True)
    recipe = models.ManyToManyField(Recipes, blank=True)
    order_send = models.DateTimeField(auto_now_add=True)
    order_start = models.DateTimeField(auto_now_add=True)
    order_finish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)


class UserFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.OneToOneField(UserOrders, on_delete=models.DO_NOTHING, default=None)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class CookFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(UserOrders, on_delete=models.DO_NOTHING, default=None)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        UserFood.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=User)
