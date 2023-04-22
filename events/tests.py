from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='kelly', password='letmein')

    def test_can_list_events(self):
        kelly = User.objects.get(username='kelly')
        Event.objects.create(owner=kelly, title='event title')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_event(self):
        response = self.client.post('/events/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Event.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_create_event(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.post(
            '/events/', {'title': 'a title', 'tags': 'tag'}
        )
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EventDetailViewTests(APITestCase):

    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        Event.objects.create(
            owner=kelly,
            title='a title',
            description='kellys event',
            tags='tag'
        )
        Event.objects.create(
            owner=greg,
            title='another title',
            description='gregs content',
            tags='sport'
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_event_using_invalid_id(self):
        response = self.client.get('/events/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/events/1/', {'title': 'an edited title', 'tags': 'tag'}
        )
        event = Event.objects.filter(pk=1).first()
        self.assertEqual(event.title, 'an edited title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_post(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put('/events/2/', {'title': 'an edited title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_event(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/events/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someone_elses_event(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/events/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
