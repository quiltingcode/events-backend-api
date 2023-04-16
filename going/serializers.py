from rest_framework import serializers
from .models import Going


class GoingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Going
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]