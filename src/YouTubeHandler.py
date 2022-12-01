# (pip install google-api-python-client) is needed
from googleapiclient.discovery import build
import matplotlib.pyplot as plt


class YouTubeHandler:
    # Youtube api key
    yt_api_key = 'AIzaSyC9NKG4azgED3XZDhxEhuVz2rjPoQUcZKk'

    # Default playlist(YouTube's The Hit List)
    playlist_id = 'RDCLAK5uy_kmPRjHDECIcuVwnKsx2Ng7fyNgFKWNJFs'

    def __init__(self):
        self.yt = build('youtube', 'v3', developerKey=self.yt_api_key)

    def init_playlist(self, id: str = playlist_id):
        """
        Description:
        ------------
        This function initialized the playlist.
        """
        nextPageToken = None
        self.playlist = dict()
        while True:
            playlist_request = self.yt.playlistItems().list(
                part='snippet',
                playlistId=id,
                maxResults=50,
                pageToken=nextPageToken
            )
            self.playlist = playlist_request.execute()
            nextPageToken = self.playlist.get('nextPageToken')
            if not nextPageToken:
                break

    def get_video_ids(self):
        """
        Description:
        ------------
        Get the video ids from the playlist.

        Return:
        -------
        A list of ids of videos from the playlist.
        """
        video_ids = []
        for item in self.playlist['items']:
            video_ids.append(item['snippet']['resourceId']['videoId'])
        return video_ids

    def get_titles(self):
        """
        Description:
        ------------
        Get the video titles from the playlist.

        Return:
        -------
        A list of video titles from the playlist.
        """
        titles = []
        for item in self.playlist['items']:
            titles.append(item['snippet']['title'])
        return titles

    def get_views(self):
        """
        Description:
        ------------
        Get the view count of videos from the playlist.

        Return:
        -------
        A list of the view count of the videos from the playlist.
        """
        views = []
        video_ids = self.get_video_ids()
        video_request = self.yt.videos().list(
            part='statistics',
            id=','.join(video_ids)
        )

        video_response = video_request.execute()
        for item in video_response['items']:
            video_vc = item['statistics']['viewCount']
            views.append(int(video_vc))
        return views

    def plot_playlist(self):
        """
        Description:
        ------------
        Plots out the view count of each video in the playlist into a bar graph.
        """
        titles = self.get_titles()
        views = self.get_views()
        fig, ax = plt.subplots(figsize=(40, 10))
        ax.bar(titles, views)
        plt.xticks(rotation=90)
        plt.xlabel('Video Title')
        plt.ylabel('View Count (in hundred millions)')
        plt.title('Current Popular Songs on YouTube and Their View Counts')
        plt.show()
