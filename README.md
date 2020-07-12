# youtube-video-search
# Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Basic Requirements:
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimised.


# Solution Description
1. I have created a django application named fmp_youtube containing an app youtube.
3. ## Running Instructions

    ### Terminal 1

    `virtualenv shubhanshu_fmp_youtube_search -p python3`

    `cd shubhanshu_fmp_youtube_search`

    `source bin/activate`

    extract zip content in this folder here, `youtube-video-search` folder from zip file should be extracted here

    `cd youtube-video-search`

    `pip install -r requirements.txt`

    `python manage.py makemigrations`

    `python manage.py migrate`

    `python manage.py runserver`

    ### Terminal 2
    `cd shubhanshu_interviews_booking`

    `source bin/activate`

    `cd ik_backend`

    `python tests.py`

# Future Scope
