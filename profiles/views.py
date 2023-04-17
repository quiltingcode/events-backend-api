
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from events_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
