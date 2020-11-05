from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Adapted from: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.TextField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # instance.userprofile.save()
    else:
        # UserProfile.objects.create(user=instance)
        instance.userprofile.save()
