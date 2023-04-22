from django.contrib.auth.models import User
from .models import Event
from .models import Review
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewsListViewTests(APITestCase):
    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        event_a = Event.objects.create(owner=kelly, title='a fun event')

    def test_can_list_reviews(self):
        kelly = User.objects.get(username='kelly')
        event_a = Event.objects.get(id=1)
        Review.objects.create(
            owner=kelly, event=event_a, review='a positive review', rating='5'
        )
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_review(self):
        event_a = Event.objects.get(id=1)
        response = self.client.post(
            '/reviews/', {'event': event_a, 'review': 'rubbish', 'rating': '3'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Review.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_create_review(self):
        self.client.login(username='greg', password='pass')
        event_a = Event.objects.get(id=1)
        current_user = User.objects.get(username='greg')
        response = self.client.post(
            '/reviews/', {
                'owner': current_user,
                'event': 1,
                'review': 'rubbish',
                'rating': '1'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        count = Review.objects.count()
        self.assertEqual(count, 1)


class ReviewsDetailViewTests(APITestCase):

    def setUp(self):
        kelly = User.objects.create_user(username='kelly', password='letmein')
        greg = User.objects.create_user(username='greg', password='pass')
        event_a = Event.objects.create(owner=kelly, title='a fun event')
        event_b = Event.objects.create(owner=greg, title='a rubbish event')
        Review.objects.create(
            owner=kelly,
            event=event_a,
            review='a positive review',
            rating='5'
        )
        Review.objects.create(
            owner=greg,
            event=event_b,
            review='a negative review',
            rating='1'
        )

    def test_cant_retrieve_review_using_invalid_id(self):
        response = self.client.get('/reviews/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_review_using_valid_id(self):
        response = self.client.get('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_own_review(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/reviews/1/', {'review': 'Ive changed my mind', 'rating': '2'}
        )
        review = Review.objects.filter(pk=1).first()
        self.assertEqual(review.review, 'Ive changed my mind')
        self.assertEqual(review.rating, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_review(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.put(
            '/reviews/2/', {'review': 'Change gregs review', 'rating': '4'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_review(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_someone_elses_review(self):
        self.client.login(username='kelly', password='letmein')
        response = self.client.delete('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_review_the_same_event_twice(self):
        self.client.login(username='kelly', password='letmein')
        current_user = User.objects.get(username='kelly')
        event_a = Event.objects.get(id=1)
        response = self.client.post(
            '/reviews/', {
                'owner': current_user,
                'event': 1,
                'review': 'a second review',
                'rating': '3'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
