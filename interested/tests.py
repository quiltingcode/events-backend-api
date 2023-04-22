from django.contrib.auth.models import User
from .models import Event
from .models import Interested
from rest_framework import status
from rest_framework.test import APITestCase


class InterestedListViewTests(APITestCase):
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        event_a = Event.objects.create(owner=kelly, title='a fun event')

    def test_can_list_interested(self):
        kelly = User.objects.get(username='kelly')
        event_a = Event.objects.get(id=1)
        Interested.objects.create(owner=kelly, event=event_a)
        response = self.client.get('/interested/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_interested(self):
        event_a = Event.objects.get(id=1)
        response = self.client.post('/interested/', {'event': event_a})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Interested.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_post_interested(self):
        self.client.login(username='kelly', password='letmein')
        event_a = Event.objects.get(id=1)
        current_user = User.objects.get(username='kelly')
        response = self.client.post(
            '/interested/', {'owner': current_user, 'event': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class InterestedDetailViewTests(APITestCase):

    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        event_a = Event.objects.create(owner=kelly, title='a fun event')
        event_b = Event.objects.create(owner=greg, title='a rubbish event')
        Interested.objects.create(owner=kelly, event=event_a)
        Interested.objects.create(owner=greg, event=event_b)

    def test_cant_retrieve_interested_using_invalid_id(self):
        response = self.client.get('/interested/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_interested_using_valid_id(self):
        response = self.client.get('/interested/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_delete_own_interested(self):
        self.client.login(username='kelly', password='letmein')
        current_user = User.objects.get(username='kelly')
        response = self.client.delete('/interested/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_in_user_cant_delete_someone_elses_interested(self):
        self.client.login(username='kelly', password='letmein')
        current_user = User.objects.get(username='kelly')
        response = self.client.delete('/interested/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_post_interested_to_the_same_event_twice(self):
        self.client.login(username='kelly', password='letmein')
        current_user = User.objects.get(username='kelly')
        event_a = Event.objects.get(id=1)
        response = self.client.post(
            '/interested/', {'owner': current_user, 'event': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
