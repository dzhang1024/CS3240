from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import UserProfile
from django.urls import reverse_lazy


def home(request):
    return render(request, 'home/homescreen.html')


def profile(request):
    return render(request, 'profile/profile.html')


class UpdateProfileView(CreateView):
    model = UserProfile
    fields = ['street_address', 'city', 'state', 'zip_code', 'phone_number']
    template_name = 'profile/update_profile.html'
    success_url = '/profile'
