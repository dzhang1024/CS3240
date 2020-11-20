from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Issue, UserProfile
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin


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


class IssueList(generic.ListView):
    model = Issue
    template_name = 'issues/issues.html' 
    context_object_name = 'all_issues'


class IssueDetail(generic.DetailView):
    model = Issue
    template_name = 'issues/issues_detail.html'


class SubmitIssue(SuccessMessageMixin, CreateView): #use a createview form to allow users to submit new issues
    model = Issue
    fields = ['issue_name', 'description', 'email_template', 'image']
    template_name = 'issues/submit_issue.html'
    success_url = reverse_lazy('home:issues')
    success_message = "Thanks for submitting a new issue! It is now pending admin approval."


@login_required
def contact(request, pk): #this is the views page that controls what we see in terms of forms
    if request.method == 'GET':
        issueName = Issue.objects.get(pk=pk)
        senderName = request.user.get_full_name
        template = Issue.objects.get(pk=pk).email_template
        form = ContactForm(initial={'message': template, 'subject': issueName, 'sender': senderName})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = form.cleaned_data['recipient_email']
            sender = form.cleaned_data['sender']
            try: 
                #this sends the email with the subject line as desired
                #recipient is filled out
                send_mail('Hoos Listening: ' + subject, message + '\n \n' + 'Best regards,\n' + sender, "Hoos Listening <civic@hooslistening.email>", [recipient_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'issues/email_success.html') #redirects to some success page (for now)
    return render(request, 'issues/email_page.html', {'form': form})


@login_required
def success(request, pk):
    return render(request, 'issues/email_success.html')

