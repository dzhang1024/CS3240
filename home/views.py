from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Issue, Email
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home/homescreen.html')

class IssueList(generic.ListView):
    model = Issue
    template_name = 'issues/issues.html'
    context_object_name = 'all_issues'

class IssueDetail(generic.DetailView):
    model = Issue
    template_name = 'issues/issues_detail.html'

class SubmitIssue(CreateView): #use a createview form to allow users to submit new issues
    model = Issue
    fields = ['issue_name', 'description', 'category']
    template_name = 'issues/submit_issue.html'
    success_url = reverse_lazy('home:issues')

class EmailIssue(CreateView):
    model = Email
    fields = ['user_name', 'email_comment']
    template_name = 'issues/email_page.html'
    success_url = reverse_lazy('home:issues')
    