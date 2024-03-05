"""
Tests for Models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):

    def test_create_user_with_email_succesfull(self):
        "test creating a user with an email is succesfull"
        email = 'test@example.com'
        password = 'testpasscode1'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_emails_are_normalized_correctly(self):
        """Test that user emails are normalized as expected."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='test@123456'
            )
            self.assertEqual(user.email, expected_email)

    def test_create_user_without_email_should_fail(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email='',
                password='test@123456'
                )

    def test_create_superuser(self):
        """
        test creating a superuser
        """
        email = 'test@example.com'
        password = 'test@123456'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
