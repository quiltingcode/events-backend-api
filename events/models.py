from django.db import models
from django.contrib.auth.models import User
from datetime import date
from taggit.managers import TaggableManager

EVENT_CATEGORIES = (
    ("Sport", "Sport"),
    ("Music", "Music"),
    ("Culture", "Culture"),
    ("Family", "Family"),
    ("Kids", "Kids"),
    ("Education", "Education"),
)


class Event(models.Model):

    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_giz2az', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='Normal'
    )
    event_date = models.DateField(default=date.today)
    tags = TaggableManager(
        help_text='A comma-separated list of tags',
        blank=True,
        verbose_name='Tags'
    )
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Culture'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
