from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer


class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(
            events, many=True, context={'request': request}
        )
        return Response(serializer.data)
