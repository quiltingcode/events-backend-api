from rest_framework import serializers
from .models import Going
from django.db import IntegrityError


class GoingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Going
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already going!'
            })
