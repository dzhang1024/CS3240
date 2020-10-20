from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Issue 

def home(request):
    return render(request, 'home/homescreen.html')

def issues(request):
    all_issues = Issue.objects.all()
    return render(request, 'issues/issues.html', {'issues': all_issues})