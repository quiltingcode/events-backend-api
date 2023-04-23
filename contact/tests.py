from django.contrib.auth.models import User
from .models import Contact
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ContactListViewTests(APITestCase):
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        gregs_profile = Profile.objects.get(owner=greg)
        kellys_profile = Profile.objects.get(owner=kelly)

    def test_can_list_contacts(self):
        kelly = User.objects.get(username='kelly')
        greg = User.objects.get(username='greg')
        gregs_profile = Profile.objects.get(id=2)

        Contact.objects.create(
            owner=kelly, profile=gregs_profile, message='hello'
        )
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_contact(self):
        current_user = User.objects.get(username='kelly')
        greg = User.objects.get(username='greg')
        profile = Profile.objects.get(pk=2)
        response = self.client.post(
            '/contact/', {'owner': current_user, 'profile': greg, 'message': 'boo'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_post_contact(self):
        self.client.login(username='kelly', password='letmein')
        current_user = User.objects.get(username='kelly')
        greg = User.objects.get(username='greg')
        profile = Profile.objects.get(pk=2)
        response = self.client.post(
            '/contact/', {'owner': current_user, 'profile': greg, 'message': 'boo'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)