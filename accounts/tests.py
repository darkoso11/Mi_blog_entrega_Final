from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class AccountTests(TestCase):
    def test_login_page_keeps_blog_name_in_navigation(self):
        response = self.client.get(reverse('login'))

        self.assertContains(
            response,
            '<a class="brand" href="/">Blog</a>',
            html=True,
        )

    def test_profile_is_created_when_user_is_created(self):
        user = User.objects.create_user(username='ana', password='clave-segura')

        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_register_view_creates_user_and_profile(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'nuevo',
                'email': 'nuevo@example.com',
                'password1': 'Clave-Segura-123',
                'password2': 'Clave-Segura-123',
            },
        )

        user = User.objects.get(username='nuevo')
        self.assertRedirects(response, reverse('profile'))
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_logged_user_can_update_profile(self):
        user = User.objects.create_user(
            username='ana',
            email='ana@example.com',
            password='clave-segura',
        )
        self.client.login(username='ana', password='clave-segura')

        response = self.client.post(
            reverse('profile_edit'),
            {
                'username': 'ana_actualizada',
                'first_name': 'Ana',
                'last_name': 'Lopez',
                'email': 'ana.lopez@example.com',
                'bio': 'Desarrolladora Django.',
            },
        )

        user.refresh_from_db()
        user.profile.refresh_from_db()
        self.assertRedirects(response, reverse('profile'))
        self.assertEqual(user.username, 'ana_actualizada')
        self.assertEqual(user.first_name, 'Ana')
        self.assertEqual(user.profile.bio, 'Desarrolladora Django.')
