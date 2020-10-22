from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic 
from django.views.generic.edit import CreateView
from .models import Issue 

def home(request):
    return render(request, 'home/homescreen.html')

class IssueList(generic.ListView):
    model = Issue
    template_name = 'issues/issues.html' 
    context_object_name = 'all_issues'

def detail(request, slug):
    obj = get_object_or_404(Issue, slug=slug)
    return render(request, 'issues/issues_detail.html', {'issue': obj})

class SubmitIssue(CreateView): #use a createview form to allow users to submit new issues
    model = Issue
    fields = ['issue_name', 'description', 'category']
    template_name = 'issues/submit_issue.html'
    success_url = '/issues'
    