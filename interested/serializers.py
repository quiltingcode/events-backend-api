from rest_framework import serializers
from .models import Interested


class InterestedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interested
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]