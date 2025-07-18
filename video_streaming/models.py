from django.db import models
from taggit.managers import TaggableManager

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    status_emision = models.BooleanField(default="False")
    labels = TaggableManager()

    def __str__(self):
        return self.title