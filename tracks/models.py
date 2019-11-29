from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
# Everytime you make a new model, you must "python manage.py makemigrations" and then "migrate"
class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=30, default="")
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey('tracks.Track', related_name='likes', on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    music_time = models.IntegerField()
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey('tracks.Track', related_name='comments', on_delete=models.CASCADE)