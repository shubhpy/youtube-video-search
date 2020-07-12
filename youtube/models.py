from django.db import models


class YoutubeVideo(models.Model):
    videoId = models.CharField(unique=True, max_length=100)
    publishedAt = models.DateTimeField()
    title = models.CharField(max_length=1000)
    description = models.TextField()


class YoutubeVideoThumbails(models.Model):
    DEFAULT = 'default'
    MEDIUM = 'medium'
    HIGH = 'high'
    STANDARD = 'standard'
    MAXRES = 'maxres'

    TYPE_CHOICES = (
        (DEFAULT, DEFAULT),
        (MEDIUM, MEDIUM),
        (HIGH, HIGH),
        (STANDARD, STANDARD),
        (MAXRES, MAXRES),
    )

    youtubeVideoId = models.ForeignKey(YoutubeVideo, related_name='thumbnails', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=DEFAULT)
    url = models.URLField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()


class CronConfig(models.Model):
    startFromPublishedAt = models.DateTimeField()
