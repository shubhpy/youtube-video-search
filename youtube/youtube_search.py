# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python




def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyBc0JmhoHkkL0etAAy-pelBqYYxEoMLbNc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        q='official',
        part='snippet',
        type='video',
        order='date',
        publishedAfter='2020-07-11T00:00:00Z',
        maxResults=50
    )
    response = request.execute()
    print(response)

MAX_COUNT = 50
nextPageToken =  None
search_by = 'machine learning tutorial'
while True:
    req = youtube.search().list(q=search_by, part='snippet', type='video', maxResults=MAX_COUNT, pageToken=nextPageToken)
    res = req.execute()
    nextPageToken = res['nextPageToken']
    items = res['items']
    if res['nextPageToken'] == None:
        break; # exit from the loop
    for each_item in items:
        #store in DB or file or print the same.
        print (each_item)

if __name__ == "__main__":
    main()
