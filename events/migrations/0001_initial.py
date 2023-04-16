# Generated by Django 3.2.18 on 2023-04-15 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_post_giz2az', upload_to='images/')),
                ('event_date', models.DateField(blank=True)),
                ('tags', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Sport', 'Sport'), ('Music', 'Music'), ('Culture', 'Culture'), ('Family', 'Family'), ('Kids', 'Kids'), ('Education', 'Education')], default='Culture', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]