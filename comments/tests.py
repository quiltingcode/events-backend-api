from django.contrib.auth.models import User
from .models import Event
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentsListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        event_a = Event.objects.create(owner=kelly, title='a fun event')

    def test_can_list_comments(self):
        kelly = User.objects.get(username='kelly')
        event_a = Event.objects.get(id=1)
        Comment.objects.create(
            owner=kelly, event=event_a, content='a positive comment'
        )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_comment(self):
        event_a = Event.objects.get(id=1)
        response = self.client.post(
            '/comments/', {'event': event_a, 'content': 'comment'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Comment.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_post_comment(self):
        self.client.login(username='kelly', password='letmein')
        event_a = Event.objects.get(id=1)
        current_user = User.objects.get(username='kelly')
        response = self.client.post(
            '/comments/', {
                'owner': current_user, 'event': 1, 'content': 'comment'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentsDetailViewTests(APITestCase):
    """
    Tests for the Comment model detail view
    """
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        event_a = Event.objects.create(owner=kelly, title='a fun event')
        event_b = Event.objects.create(owner=greg, title='a rubbish event')
        Comment.objects.create(
            owner=kelly, event=event_a, content='a positive comment'
        )
        Comment.objects.create(
            owner=greg, event=event_b, content='a negative comment'
        )

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_own_comment(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/comments/1/', {'content': 'not a positive comment anymore'}
        )
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'not a positive comment anymore')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_comment(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/comments/2/', {'content': 'an edited content'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_comment(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someone_elses_comment(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
