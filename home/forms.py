from .models import UserProfile
from django import forms
from django.contrib.auth.models import User

# Adapted from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('street_address', 'city', 'state', 'zip_code', 'phone_number')


# created form that has subject recipient and message
class ContactForm(forms.Form):
    recipient_email = forms.EmailField(required=True)
    sender = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
