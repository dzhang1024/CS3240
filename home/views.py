from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def home(request):
    return render(request, 'home/homescreen.html')

def issues(request):
    return render(request, 'issues/issues.html')