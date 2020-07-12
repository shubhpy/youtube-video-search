import requests

print("---------------------------TestCase 1--------------------------")
print("Printing all videos fetched [PAGINATED]")
print(requests.get('http://127.0.0.1:8000/youtube-videos/').text)
print()

print("---------------------------TestCase 2--------------------------")
print("Printing next 10 videos")
print(requests.get('http://127.0.0.1:8000/youtube-videos/?limit=10&offset10').text)
print()

print("---------------------------TestCase 3--------------------------")
print("Searching for fantasy football")
print(requests.get('http://127.0.0.1:8000/youtube-videos/search?q=fantasy football').text)
print()

print("---------------------------TestCase 4--------------------------")
print("Searching for fantasy football with limit 1")
print(requests.get('http://127.0.0.1:8000/youtube-videos/search?q=fantasy football&limit=1').text)
print()
