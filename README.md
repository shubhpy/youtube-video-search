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

    `git clone https://github.com/shubhpy/youtube-video-search.git`

    `cd youtube-video-search`

    `docker build . -t fmp_youtube`

    `docker run -it -p 8000:8000 fmp_youtube`

    ### Terminal 2
    `cd youtube-video-search`

    `python tests.py`

# Future Scope
