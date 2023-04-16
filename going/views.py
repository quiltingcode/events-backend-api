from rest_framework import generics, permissions
from events_api.permissions import IsOwnerOrReadOnly
from going.models import Going
from going.serializers import GoingSerializer


class GoingList(generics.ListCreateAPIView):
    serializer_class = GoingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Going.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
