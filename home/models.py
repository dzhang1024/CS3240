from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify

# Adapted from: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=11, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True)
    objects=models.Manager()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # instance.userprofile.save()
    else:
        # UserProfile.objects.create(user=instance)
        instance.userprofile.save()


# Create your models here.


class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    email_template = models.TextField(default="")
    approval = models.BooleanField(default=False)
    # slug = models.SlugField(default='', editable=False, max_length=200, null = False)

    def __str__(self):
        # self.slug = slugify(self.issue_name, allow_unicode=True)
        return self.issue_name

