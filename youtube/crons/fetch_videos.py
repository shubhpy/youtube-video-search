import os
import random

import googleapiclient.discovery
import googleapiclient.errors

from youtube.models import YoutubeVideo, YoutubeVideoThumbails


class YoutubeV3VideoFetcher():
    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.start_from_publishedAt = '2020-07-10T00:00:00Z'
        api_key = "AIzaSyBc0JmhoHkkL0etAAy-pelBqYYxEoMLbNc"
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey=api_key)

    def get_next_api_token(self):
        pass

    def get_random_search_term(self):
        search_terms = ('official', 'football', 'cricket',
                        'corona', 'india', 'comedy')
        return search_terms[random.randint(0, len(search_terms) - 1)]

    def save_search_item_as_video_with_description(self, item):
        videoId = item['id']['videoId']
        publishedAt = item['snippet']['publishedAt']
        title = item['snippet']['title']
        description = item['snippet']['description']

        if not YoutubeVideo.objects.filter(videoId=videoId).first():
            video = YoutubeVideo(
                publishedAt=publishedAt,
                title=title,
                description=description,
                videoId=videoId,
            )
            video.save()

            for thumbnailType, thumbnailDetails in item['snippet'].get('thumbnails', []):
                YoutubeVideoThumbails(
                    youtubeVideoId=video,
                    type=thumbnailType,
                    url=thumbnailDetails['url'],
                    width=thumbnailDetails['width'],
                    height=thumbnailDetails['height'],
                ).save()

            try:
                request2 = self.youtube.videos().list(
                    part='snippet', fields='items(snippet(description))', id=videoId)
                response2 = request2.execute()
                if len(response2.get('items', [])) and response2['items'][0].get('snippet', {}).get('description', None):
                    video.description = response2['items'][0]['snippet']['description']
                    video.save()
            except Exception as e:
                print(e.__str__())

    def search_videos(self):
        try:
            while True:
                search_by = self.get_random_search_term()
                nextPageToken = None
                MAX_COUNT = 50

                request = self.youtube.search().list(
                    q=search_by,
                    part='snippet',
                    type='video',
                    order='date',
                    publishedAfter=self.start_from_publishedAt,
                    maxResults=MAX_COUNT,
                    pageToken=nextPageToken,
                )
                response = request.execute()
                nextPageToken = response['nextPageToken']
                items = response['items']
                for item in items:
                    self.save_search_item_as_video_with_description(item)
                if res['nextPageToken'] == None:
                    break
        except OSError:
            print("error")
