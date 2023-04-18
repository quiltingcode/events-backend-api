from rest_framework import serializers
from .models import Event
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

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'title', 'description', 'image', 'event_date',
            'tags', 'category', 'is_owner', 'profile_id',
            'profile_image', 'image_filter'
        ]
