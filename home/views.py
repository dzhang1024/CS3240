from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Issue
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
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

def contact(request, pk):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            #sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            try: 
                send_mail(subject, message, 'dz9sb@virginia.edu', [recipient], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('success')
    return render(request, 'issues/email_page.html', {'form': form})

def success(request):
    return HttpResponse('success')

    