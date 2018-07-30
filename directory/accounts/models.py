from django.db import models
from django.contrib import auth
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    chapter_pledged = models.CharField(max_length=156, blank=True, null=True)
    year_pledged = models.IntegerField(blank=True, null=True)
    current_chapter = models.CharField(max_length=156, blank=True, null=True,)
    major = models.CharField(max_length=256, blank=True, null=True,)
    year_graduated = models.IntegerField(blank=True, null=True)
    current_position = models.CharField(max_length=256, blank=True, null=True,)
    linkedin = models.CharField(max_length=256, blank=True, null=True,)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    other_info = models.CharField(max_length=560, blank=True, null=True)
    business = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return "@{}".format(self.username)