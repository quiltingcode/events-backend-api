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
