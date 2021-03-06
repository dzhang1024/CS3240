# /***************************************************************************************
# *  REFERENCES
# *  Title: How to redirect to previous page in Django after POST request
# *  Author: Oleg, Antoine Pinsard
# *  Date: 11/21/2020
# *  Code version: N/A
# *  URL: https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request
# *  Software License: CC BY-SA 3.0
# *
# *  Title: How to Extend Django User Model
# *  Author: Vitor Freitas
# *  Date: 11/05/2020
# *  Code version: N/A
# *  URL: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# *  Software License: CC BY-NC-SA 3.0
# *
# *  Title: How to email a Django form 
# *  Author: Will Vincent
# *  Date: 07/17/2020
# *  Code version: N/A
# *  URL: https://learndjango.com/tutorials/django-email-contact-form 
# *  Software License: N/A
# ***************************************************************************************/


from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    return render(request, 'home/homescreen.html')


@login_required
def profile(request):
    return render(request, 'profile/profile.html', {'userprofile': request.user.userprofile})


# Derived from Reference 2: "How to Extend Django User Model"
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
            messages.error(request, ("Invalid data received. Please try again."))
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
def saved_issues(request):
    return render(request, 'issues/saved_issues.html', {'userprofile': request.user.userprofile})


# Derived from Reference 1: "How to redirect to previous page in Django after POST request"
@login_required
def save_issue(request, pk):
    if request.method == 'POST':
        issue_to_save = Issue.objects.get(pk=pk)
        request.user.userprofile.saved_issues.add(issue_to_save)
        messages.add_message(request, messages.INFO, 'Saved Issue to profile!')
        nextlink = request.POST.get('next', '/')
        return HttpResponseRedirect(nextlink)
    else:
        return redirect('home:issues')


@login_required
def remove_issue(request, pk):
    if request.method == 'POST':
        issue_to_remove = Issue.objects.get(pk=pk)
        request.user.userprofile.saved_issues.remove(issue_to_remove)
        messages.add_message(request, messages.INFO, 'Removed Issue from profile!')
        nextlink = request.POST.get('next', '/')
        return HttpResponseRedirect(nextlink)
    else:
        return redirect('home:issues')


#Derived from Reference 3: "How to email a Django form"
#Modified so that it will prepopulate 
@login_required
def contact(request, pk):
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
                send_mail('Hoos Listening: ' + subject, message + '\n \n' + 'Best regards,\n' + sender + '\n\n' + request.user.email, "Hoos Listening <civic@hooslistening.email>", [recipient_email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'issues/email_success.html') #redirects to some success page (for now)
    return render(request, 'issues/email_page.html', {'form': form})


@login_required
def success(request, pk):
    return render(request, 'issues/email_success.html')

