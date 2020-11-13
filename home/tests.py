from django.db import models
from django.test import TestCase, Client
from django.urls import reverse
from phone_field import PhoneField
from .models import Issue, UserProfile
from .forms import ContactForm
from django.contrib.auth.models import User

class IssueTestCases(TestCase):
    def setUp(self):
        Issue.objects.create(issue_name="test_issue", description="test_description", email_template="test_template", approval=True)

    def test_issue_name(self):
        test_issue = Issue.objects.get(issue_name="test_issue")
        self.assertEqual(test_issue.issue_name, "test_issue")

    def test_issue_description(self):
        test_issue = Issue.objects.get(issue_name="test_issue")
        self.assertEqual(test_issue.description, "test_description")

    def test_issue_email_template(self):
        test_issue_email_template = Issue.objects.get(issue_name="test_issue")
        self.assertEqual(test_issue_email_template.email_template, "test_template")

    def test_issue_approval(self):
        test_issue_approval = Issue.objects.get(issue_name="test_issue")
        self.assertTrue(test_issue_approval.approval, True)


class IssueViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        Issue.objects.create(issue_name="test_issue", description="test_description", email_template="test_template", approval=True)
        self.test_issue = Issue.objects.get(issue_name="test_issue")

    def test_issues_page(self):
        response = self.client.get(reverse('home:issues'))
        self.assertEqual(response.status_code, 200) #status codes standardiszes in https look up
        self.assertNotContains(response, "Currently no issues available.")

    '''def test_issues_detail(self):
        response = self.client.get(reverse('home:issues_detail', kwargs={'pk': self.test_issue.pk}))
        self.assertEqual(response.status_code, 200) #status codes standardiszes in https look up
        self.assertNotContains(response, "Currently no issues available.")'''
    

class UserTestCases(TestCase):
    def setUp(self):
        test_user = User(username='test_user', password='password')
        test_user.first_name = 'test_name'
        test_user.last_name = 'test_name'
        test_user.email = 'test_email'
        test_user.save()
        test_userprofile = UserProfile(user=test_user, street_address="test_street", city="test_city", state="test_state", zip_code="20191", phone_number="703test")
        test_userprofile.save()

    def test_user_street_address(self):
        test_user = UserProfile.objects.get(street_address="test_street")
        self.assertEqual(test_user.street_address, "test_street")

    def test_user_city(self):
        test_city = UserProfile.objects.get(city="test_city")
        self.assertEqual(test_city.city, "test_city")

    def test_user_state(self):
        test_state = UserProfile.objects.get(state="test_state")
        self.assertEqual(test_state.state, "test_state")

    def test_user_zip_code(self):
        test_zip_code = UserProfile.objects.get(zip_code="20191")
        self.assertEqual(test_zip_code.zip_code, "20191")

    def test_user_phone_number(self):
        test_phone_number = UserProfile.objects.get(phone_number="703test")
        self.assertEqual(test_phone_number.phone_number, "703test")

class ContactFormTests(TestCase):
    def setUp(self):
        self.test_form = ContactForm()
        self.test_form.recipient_email = "test_email"
        self.test_form.sender = "test_sender"
        self.test_form.subject = "test_subject"
        self.test_form.message = "test_message"

    def form_isvalid(self):
        self.assertTrue(self.test_form.isvalid())

    def test_email(self):
        self.assertEqual(self.test_form.recipient_email, "test_email")

    def test_sender(self):
        self.assertEqual(self.test_form.sender, "test_sender")

    def test_subject(self):
        self.assertEqual(self.test_form.subject, "test_subject")

    def test_message(self):
        self.assertEqual(self.test_form.message, "test_message")
