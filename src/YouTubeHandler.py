#(pip install google-api-python-client) is needed
import os
from googleapiclient.discovery import build
import matplotlib.pyplot as plt

class YouTubeHandler:
    #Youtube api key
    yt_api_key = 'AIzaSyC9NKG4azgED3XZDhxEhuVz2rjPoQUcZKk'

    #Default playlist(YouTube's The Hit List)
    playlist_id = 'RDCLAK5uy_kmPRjHDECIcuVwnKsx2Ng7fyNgFKWNJFs'

    def __init__(self):
        self.yt = build('youtube', 'v3', developerKey = self.yt_api_key)

    def init_playlist(self, id: str = playlist_id):
        nextPageToken = None
        self.playlist = dict() 
        while True:
            playlist_request = self.yt.playlistItems().list(
                part= 'snippet',
                playlistId= id,
                maxResults= 50,
                pageToken= nextPageToken
            )
            self.playlist = playlist_request.execute()
            nextPageToken = self.playlist.get('nextPageToken')
            if not nextPageToken:
                break

    def get_video_ids(self):
        video_ids = []
        for item in self.playlist['items']:
            video_ids.append(item['snippet']['resourceId']['videoId'])
        return video_ids

    def get_titles(self):
        titles = []
        for item in self.playlist['items']:
            titles.append(item['snippet']['title'])
        return titles
        
    def get_views(self):
        views = []
        video_ids = self.get_video_ids()
        video_request = self.yt.videos().list(
            part= 'statistics',
            id= ','.join(video_ids)
        )

        video_response = video_request.execute()
        for item in video_response['items']:
            video_vc = item['statistics']['viewCount']
            views.append(int(video_vc))
        return views

    def plot_playlist(self):
        titles = self.get_titles()
        views = self.get_views()
        fig, ax = plt.subplots(figsize = (40, 10))
        ax.bar(titles, views)
        plt.xticks(rotation=90)
        plt.xlabel('Video Title')
        plt.ylabel('View Count (in hundred millions)')
        plt.title('Current Popular Songs on YouTube and Their View Counts')
        plt.show()