from rest_framework import serializers
from .models import Interested
from django.db import IntegrityError


class InterestedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interested
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already interested!'
            })
