from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify

# Adapted from: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents/', default=None, blank=True)
    description = models.CharField(max_length=100)
    email_template = models.TextField(default="")
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.issue_name

# ManyToMany for saving issues derived from https://stackoverflow.com/questions/49098606/how-to-save-a-users-favorite-posts-in-django
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=11, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True)
    objects = models.Manager()
    saved_issues = models.ManyToManyField(Issue, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
