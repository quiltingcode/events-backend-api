from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Review(models.Model):
    """
    Review model, related to Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='reviews', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()
    rating = models.IntegerField()

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f"{self.owner}'s review"
