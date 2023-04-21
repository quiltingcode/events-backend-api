from rest_framework import generics, permissions, filters
from events_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django.db.models import Count, Avg
from django_filters.rest_framework import DjangoFilterBackend


class ReviewList(generics.ListCreateAPIView):
    """
    List reviews or create a review if logged in.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
