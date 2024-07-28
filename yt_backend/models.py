from django.db import models

# Create your models here.

class YtVideos(models.Model):
    title = models.CharField(max_length = 1000)
    channel_name = models.CharField(max_length = 250)
    views = models.CharField(max_length = 10)
    relative_time = models.IntegerField()
    relative_time_unit = models.CharField(max_length = 10)
    video_file = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.title 