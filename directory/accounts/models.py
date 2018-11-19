from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.


# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return "@{}".format(self.username)

ORGINIZATION_CHOICES = (
    ('Phi Beta Sigma','Phi Beta Sigma'),
    ('Zeta Phi Beta', 'Zeta Phi Beta'),
)


class Profile(AbstractUser):
    orginization = models.CharField(max_length=128, choices=ORGINIZATION_CHOICES, blank=True, null=True)
    chapters_pledged = models.CharField(max_length=156, blank=True, null=True)
    bio = models.CharField(max_length=560, blank=True, null=True)
    year_pledged = models.IntegerField(blank=True, null=True)
    current_chapter = models.CharField(max_length=156, blank=True, null=True, )
    major = models.CharField(max_length=256, blank=True, null=True, )
    year_graduated = models.IntegerField(blank=True, null=True)
    current_position = models.CharField(max_length=256, blank=True, null=True, )
    linkedin = models.CharField(max_length=256, blank=True, null=True, )
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    other_info = models.CharField(max_length=560, blank=True, null=True)
    business = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        return "@{}".format(self.username)

# @receiver(post_save, sender=Profile)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=Profile)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
