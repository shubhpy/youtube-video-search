from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from youtube.views import YoutubeVideoViewSet

router = routers.SimpleRouter()
router.register(r'', YoutubeVideoViewSet, basename='youtube')
urlpatterns = [
    url(r'', include(router.urls))
]