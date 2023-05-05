from rest_framework import serializers
from django.utils.dateformat import format
from .models import Event
from interested.models import Interested
from going.models import Going
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    tags = TagListSerializerField()
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url'
    )
    interested_id = serializers.SerializerMethodField()
    going_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    interested_count = serializers.ReadOnlyField()
    going_count = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    # event_date = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, event=obj
            ).first()
            return interested.id if interested else None
        return None

    def get_going_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            going = Going.objects.filter(
                owner=user, event=obj
            ).first()
            return going.id if going else None
        return None

    # def get_event_date(self, obj):
    #     return format(obj.event_date, 'j F Y')

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'title', 'description', 'image', 'event_date',
            'tags', 'category', 'is_owner', 'profile_id',
            'profile_image', 'image_filter', 'interested_id',
            'going_id', 'comments_count', 'interested_count',
            'going_count', 'review_count', 'average_rating',
        ]
