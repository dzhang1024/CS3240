from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib import messages


def home(request):
    return render(request, 'home/homescreen.html')


def profile(request):
    return render(request, 'profile/profile.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form_data = UserForm(request.POST, instance=request.user)
        profile_form_data = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form_data.is_valid() and profile_form_data.is_valid():
            user_form_data.save()
            profile_form_data.save()
            return redirect('/profile')
        else:
            messages.error(request, ("You've done goofed."))
    else:
        user_form_data = UserForm(instance=request.user)
        profile_form_data = ProfileForm(instance=request.user.userprofile)
    return render(request, '/profile/profile.html', {'user_form' : user_form_data, 'profile_form' : profile_form_data })


class UpdateProfileView(CreateView):
    model = UserProfile
    fields = ['street_address', 'city', 'state', 'zip_code', 'phone_number']
    template_name = 'profile/update_profile.html'
    success_url = '/profile'
