from rest_framework import serializers
from .models import Going
from django.db import IntegrityError


class GoingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Going model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Going
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        """
        Validation to stop a user posting going to the same event twice
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already going!'
            })
