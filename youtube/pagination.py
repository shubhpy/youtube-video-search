from rest_framework.pagination import LimitOffsetPagination


class YoutubeVideoListPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'page_size'
    offset_query_param = 'page'
    max_limit = 50
