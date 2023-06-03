from rest_framework import generics, permissions
from events_api.permissions import IsOwnerOrReadOnly
from going.models import Going
from going.serializers import GoingSerializer


class GoingList(generics.ListCreateAPIView):
    """
    List going posts or create a going post if logged in
    The perform_create method associates the going post with the logged
    in user.
    """
    serializer_class = GoingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Going.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GoingDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a going post, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GoingSerializer
    queryset = Going.objects.all()
