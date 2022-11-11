import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyHandler:
    """Handle any spotify related task in our project"""

    __client_id = "5d2671fe13644512aeb70d497c165c82"
    __client_secret = "4ae2f73b3aab4106903bc34919f04043"

    # Default playlist
    play_list = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33"
    items = list()

    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=self.__client_id, client_secret=self.__client_secret)
        self.sp = spotipy.Spotify(
            client_credentials_manager=self.client_credentials_manager)

    def init_play_list(self, url_link: str):
        """
        Description:
        ------------
        This function initialized the playlist

        Parameters:
        -----------
        - url_link (str): 
            Direct website link to that playlist on Spotify.
        """
        self.play_list = url_link
        self.items = self.sp.playlist_tracks(
            playlist_id=self.play_list)["items"]

    def get_author_uri(self):
        """
        Description:
        ------------
        Get the authors uri from the given list of songs."""
        artist_uri = list()
        for i in self.items:
            artist_uri = i['track']['artists'][0]['uri']
        return artist_uri
    
    def get_genres(self):
        #TODO get the genre of the song 
        pass

    # for i in items:
    #     artist_uri = i['track']['artists'][0]['uri']
    #     artist_info = sp.artist(artist_uri)
    #     print(f"{i['track']['name']}, {i['track']['artists'][0]['name']}", end=" ")
    #     print("(", end="")
    #     for i in artist_info['genres']:
    #         if len(artist_info['genres']) > 1:
    #             print(f"{i}", end=", ")
    #         else:
    #             print(f"{i}", end="")
    #     print(")")
    #     print("\n")
