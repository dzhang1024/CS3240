from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Issue 

def home(request):
    return render(request, 'home/homescreen.html')

def issues(request):
    all_issues = Issue.objects.all() #gets every single issue in the database and stores it 
    return render(request, 'issues/issues.html', {'issues': all_issues})

class SubmitIssue(CreateView): #use a createview form to allow users to submit new issues
    model = Issue
    fields = ['issue_name', 'description', 'category']
    template_name = 'issues/submit_issue.html'
    success_url = '/issues'
    