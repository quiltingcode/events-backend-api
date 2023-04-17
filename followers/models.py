from django.db import models
from django.contrib.auth.models import User


class Followers(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    'owner' is a User that is following a User.
    'followed' is a User that is followed by 'owner'.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
