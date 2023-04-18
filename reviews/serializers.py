from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url'
    )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'event',
            'review', 'rating', 'is_owner', 'profile_id',
            'profile_image',
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    event is a read only field so that we dont have to set it on each update
    """
    event = serializers.ReadOnlyField(source='event.id')
