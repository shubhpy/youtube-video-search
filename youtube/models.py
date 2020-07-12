from django.db import models


class YoutubeVideo(models.Model):
    publishedAt = models.DateTimeField()
    title = models.CharField(max_length=1000)
    description = models.TextField()
    videoId = models.CharField(max_length=100)


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

    youtubeVideoId = models.ForeignKey(YoutubeVideo, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=DEFAULT)
    url = models.URLField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
