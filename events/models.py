from django.db import models
from django.contrib.auth.models import User

EVENT_CATEGORIES = (
    ("Sport", "Sport"),
    ("Music", "Music"),
    ("Culture", "Culture"),
    ("Family", "Family"),
    ("Kids", "Kids"),
    ("Education", "Education"),
)


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_giz2az', blank=True
    )
    event_date = models.DateField(blank=True)
    tags = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Culture'
    )

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'
