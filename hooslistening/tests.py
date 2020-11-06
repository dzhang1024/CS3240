from django.test import TestCase
from home.models import UserProfile
from django.contrib.auth.models import User


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.userprofile.city = "Charlottesville"
        self.user.userprofile.zip_code = "22903-5555"
        self.user.userprofile.phone_number = "5551234567"

    def test_NumberEquals(self):
        self.assertEqual(self.user.userprofile.phone_number, "5551234567")

    def test_StateNone(self):
        self.assertEqual(self.user.userprofile.state, None)

