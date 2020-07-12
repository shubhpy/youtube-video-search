from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from youtube.models import YoutubeVideo, YoutubeVideoThumbails
from youtube.serializers import YoutubeVideoSerializer
from youtube.pagination import YoutubeVideoListPagination


class YoutubeVideoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = YoutubeVideo.objects
    serializer_class = YoutubeVideoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    pagination_class = YoutubeVideoListPagination
