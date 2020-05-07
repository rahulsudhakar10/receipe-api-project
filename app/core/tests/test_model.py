from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):
    def test_user_with_email(self):
        email = "rahul@gamil.com"
        password = "12345"

        user = get_user_model().objects.create_user(
           email=email,
           password=password
           )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_with_email_normilized(self):
        email = "rahul@GMAIL.COM"
        user = get_user_model().objects.create_user(
          email, '12345')

        self.assertEqual(user.email, email.lower())

    def test_user_with_no_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
              None, '12345')

    def test_user_is_superuser(self):
        email = "rahul@GMAIL.COM"
        user = get_user_model().objects.create_superuser(
          email, '12345')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
           user=sample_user(),
           name='vegan'
        )

        self.assertEqual(str(tag), tag.name)
