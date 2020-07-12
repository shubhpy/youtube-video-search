import os
import random

import googleapiclient.discovery
import googleapiclient.errors

from youtube.models import YoutubeVideo, YoutubeVideoThumbails, CronConfig


class YoutubeV3VideoFetcher():
    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"

    def get_random_api_token(self):
        api_tokens = (
            'AIzaSyBc0JmhoHkkL0etAAy-pelBqYYxEoMLbNc',
            'AIzaSyD_NDCMgtM0DN7DoM78bCMS162Z4u3uJBc',
            'AIzaSyCDQZpdD4Neocp4q2wDfdWGQqXZQaiOyMM',
            'AIzaSyCaPWKzO7o-AQWhrcGL4HYo67z4KxYfEIo',
            'AIzaSyBzprgfbjZwpKr9eQ0duVge0kyxc2EwjiI',
            'AIzaSyAmJGX_sUFDaap-8SsNwg8AmDdbEY75NwY',
            'AIzaSyBmXYxVlFr2TXLqBI3JBp1AGBecqvl3N-w',
            'AIzaSyCaCYg18s8gXidaN12NVXvSaG586rvKDVo',
            'AIzaSyCLNyOJ85JTcZdZPHKHjBHMiql43clLWE4',
            'AIzaSyCLOc-8jHLVIGNBSxvC2yVOiZPS0ndaFUA'
        )
        return api_tokens[random.randint(0, len(api_tokens) - 1)]

    def get_start_from_publishedAt(self):
        self.config = CronConfig.objects.first()
        if not self.config:
            self.config = CronConfig(startFromPublishedAt='2020-07-10T00:00:00Z')
            self.config.save()
        return self.config.startFromPublishedAt.strftime('%Y-%m-%dT%H:%M:%SZ')

    def set_start_from_publishedAt(self, latest_publishedat):
        self.config.startFromPublishedAt = latest_publishedat
        self.config.save()

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

            for thumbnailType, thumbnailDetails in item['snippet'].get('thumbnails', {}).items():
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
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey=self.get_random_api_token())
        try:
            latest_publishedat = None
            search_by = self.get_random_search_term()
            while True:
                nextPageToken = None
                MAX_COUNT = 50

                request = self.youtube.search().list(
                    q=search_by,
                    part='snippet',
                    type='video',
                    order='date',
                    publishedAfter=self.get_start_from_publishedAt(),
                    maxResults=MAX_COUNT,
                    pageToken=nextPageToken,
                )
                response = request.execute()
                nextPageToken = response['nextPageToken']
                items = response['items']
                print(f"Fetched {len(items)} items")
                for item in items:
                    if latest_publishedat is None:
                        latest_publishedat = item['snippet']['publishedAt']
                    self.save_search_item_as_video_with_description(item)
                if nextPageToken == None:
                    break
            self.set_start_from_publishedAt(latest_publishedat)
        except Exception as e:
            print(e.__str__())

def run():
    print("Started the Script")
    YVF = YoutubeV3VideoFetcher()
    YVF.search_videos()
