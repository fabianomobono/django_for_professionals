from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomuserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will", email="will@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@email.com")
        self.assertEqual(user.is_active, True)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superwill", email="superwill@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superwill")
        self.assertEqual(admin_user.email, "superwill@email.com")
        self.assertEqual(admin_user.is_active, True)
        self.assertEqual(admin_user.is_staff, True)
        self.assertEqual(admin_user.is_superuser, True)
