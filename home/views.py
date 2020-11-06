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
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home/homescreen.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html', {'userprofile': request.user.userprofile})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form_data = UserForm(request.POST, instance=request.user)
        profile_form_data = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form_data.is_valid() and profile_form_data.is_valid():
            user_form_object = user_form_data.save(commit=False)
            user_form_object.user = request.user.id
            user_form_object.save()
            profile_form_object = profile_form_data.save(commit=False)
            profile_form_object.user = User.objects.get(id=request.user.id)
            profile_form_object.save()
            return redirect('/profile')
        else:
            messages.error(request, ("You've done goofed."))
    else:
        user_form_data = UserForm(instance=request.user)
        profile_form_data = ProfileForm(instance=request.user.userprofile)
    return render(request, 'profile/update_profile.html', {'user_form': user_form_data, 'profile_form': profile_form_data})