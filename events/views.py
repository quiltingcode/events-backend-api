from rest_framework import generics, permissions, filters
from .models import Event
from .serializers import EventSerializer
from events_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count, Avg
from django_filters.rest_framework import DjangoFilterBackend


# class EventFilter(filters.FilterSet):
    # user_feed = filters.AllValuesMultipleFilter('interested__owner__profile', 'going__owner__profile')
    # my_events = filters.AllValuesMultipleFilter('interested__owner__profile', 'going__owner__profile')
    # profile_posts = filters.filterset_fields('owner__profile')
    # category_filter = filters.filterset_fields('category')


class EventList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
        going_count=Count('going', distinct=True),
        review_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # filterset_class = EventFilter
    filterset_fields = [
        'owner__followed__owner__profile',
        'interested__owner__profile',
        'going__owner__profile',
        'owner__profile',
        'category',
    ]
    search_fields = [
        'owner__username',
        'title',
        'event_date',
        'tags__name',
    ]
    ordering_fields = [
        'comments_count',
        'interested_count',
        'going_count',
        'review_count',
        'average_rating',
        'interested__created_at',
        'going__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
        going_count=Count('going', distinct=True),
        review_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating', distinct=True),
    ).order_by('-created_at')
