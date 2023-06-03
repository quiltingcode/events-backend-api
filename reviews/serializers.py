from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review
from django.db import IntegrityError


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url'
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'event',
            'review', 'rating', 'is_owner', 'profile_id',
            'profile_image',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already reviewed this event!'
            })


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    event is a read only field so that we dont have to set it on each update
    """
    event = serializers.ReadOnlyField(source='event.id')
