from googleapiclient import discovery
build = discovery.build
import os
from dotenv import load_dotenv 
load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_video(query):
    req = youtube.search().list(q=query, part='id', type='video', maxResults=10, order='viewCount')
    response = req.execute()
    videoID=response.get('items')[0]['id']['videoId']
    url = 'https://www.youtube.com/watch?v=' + str(videoID)
    return url
    