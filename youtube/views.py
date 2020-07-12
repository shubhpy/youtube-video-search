from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from youtube.models import YoutubeVideo, YoutubeVideoThumbails
from youtube.serializers import YoutubeVideoSerializer, YoutubeSearchConsumer
from youtube.pagination import YoutubeVideoListPagination
from youtube.search_utils import get_query


class YoutubeVideoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = YoutubeVideo.objects.all().order_by('-publishedAt')
    serializer_class = YoutubeVideoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    pagination_class = YoutubeVideoListPagination

    @action(methods=['GET'], detail=False, url_path="search")
    def search(self, request, *args, **kwargs):
        consumer = YoutubeSearchConsumer(data=request.query_params)
        consumer.is_valid(raise_exception=True)
        query_string = consumer.validated_data['q']

        query = get_query(query_string=query_string, search_fields=('title', 'description'))
        queryset = self.get_queryset().filter(query)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
