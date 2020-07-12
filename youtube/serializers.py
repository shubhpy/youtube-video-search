from rest_framework import serializers
from youtube.models import YoutubeVideo, YoutubeVideoThumbails


class YoutubeVideoThumbnailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideoThumbails
        fields = ('type', 'url', 'width', 'height')


class YoutubeVideoSerializer(serializers.ModelSerializer):
    thumbnails = YoutubeVideoThumbnailsSerializer(many=True, read_only=True)

    class Meta:
        model = YoutubeVideo
        fields = '__all__'
