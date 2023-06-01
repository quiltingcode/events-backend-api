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
        profile = Profile.objects.get(id=2)
        response = self.client.post(
            '/contact/', {
                'owner': current_user, 'profile': profile, 'message': 'boo'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ContactDetailViewTests(APITestCase):
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        gregs_profile = Profile.objects.get(owner=greg)
        kellys_profile = Profile.objects.get(owner=kelly)
        Contact.objects.create(
            owner=kelly, profile=gregs_profile, message='hello greg'
        )
        Contact.objects.create(
            owner=greg, profile=kellys_profile, message='hello kelly'
        )

    def test_cant_retrieve_contact_using_invalid_id(self):
        response = self.client.get('/contact/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_contact_using_valid_id(self):
        response = self.client.get('/contact/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_own_contact(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/contact/1/', {'message': 'change the message'}
        )
        contact = Contact.objects.filter(pk=1).first()
        self.assertEqual(contact.message, 'change the message')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_contact(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/contact/2/', {'message': 'how are you'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_contact(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/contact/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someone_elses_contact(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/contact/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
