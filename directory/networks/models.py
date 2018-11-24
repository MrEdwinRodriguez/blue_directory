from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
 User = get_user_model()


 class Network(models.Model):
     name = models.Charfield(max-length=255, unique=True)
     slug = models.Slugfield(allow_unicode=True, unique=True)
     descrription = models.TextField(blank=True, default='')
     description_html = models.textField(editable=False, default='', blank=True)
     members = models.ManytoManyField(User, through='NetworkMember')

     def __str__(self):
         return self.name

     def save(self, *args, **kwargs):
         self.slug.slugify(self.name)
         self.descrription_html = misaka.html(self.descrription)
         super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('networks:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']




 class NetworkMember(models.Model):
     network = models.ForeignKey(Group, related_name="memberships")
     user = models.ForeignKey(User, related_names="user_networks")


     def __str__(self):
         return self.user.username

     class Meta:
         unique_together = ('netowk, user')




