import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import operator
import pandas


class SpotifyHandler:
    """Handle any spotify related task in our project"""

    __client_id = "5d2671fe13644512aeb70d497c165c82"
    __client_secret = "4ae2f73b3aab4106903bc34919f04043"

    # Default playlist
    play_list = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33"
    items = list()

    def __init__(self):
        """
        Description:
        ------------
        Generate a new SpotifyHandler object and initialize a default playlist:
        - Top 50 Global Playlist(default): https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=4d35ac989d9e4ab2
        """
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=self.__client_id, client_secret=self.__client_secret)
        self.sp = spotipy.Spotify(
            client_credentials_manager=self.client_credentials_manager)
        self.init_play_list(self.play_list)

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

    def get_author_uri(self) -> list:
        """
        Description:
        ------------
        Get the authors uri from the given list of songs.

        Return:
        -------
        A list of authors uri
        """
        artist_uri = list()
        for i in self.items:
            artist_uri = i['track']['artists'][0]['uri']
        return artist_uri

    def get_genres(self) -> list:
        """
        Description:
        ------------
        Get the list of genres of a list of songs

        Return:
        -------
        A list of genres
        """
        genres = list()
        for i in self.items:
            artist_uri = i['track']['artists'][0]['uri']
            artist_info = self.sp.artist(artist_uri)
            for z in artist_info["genres"]:
                if len(artist_info["genres"]) >= 1:
                    genres.append(z)
        return genres

    def get_most_poplar_genre(self) -> str:
        """
        Description:
        ------------
        This method get the name of the most popular genre from a given genre list

        Return:
        -------
        The most popular genre
        """
        genres = dict()
        genre_list = self.get_genres()
        for i in genre_list:
            if i not in genres:
                genres[i] = 1
            else:
                genres[i] += 1
        genres = sorted(genres.items(), key=operator.itemgetter(1))
        return genres[-1][0]

    def generate_data_frame(self, data={"Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
                                        "Users (mm)": [77, 104, 138, 180, 232, 299, 365]}) -> pandas.DataFrame:
        """
        Description:
        ------------
        Generate a simple data frame the given data with default: {"year": [2015, 2016, 2017, 2018, 2019, 2020, 2021],
                                    "Users (mm)":[77, 104, 138, 180, 232, 299, 365]}
        
        Param:
        ------
        data - used to create data frame

        Return:
        -------
        The generated DataFrame
        """
        pd = pandas.DataFrame(data)
        return pd

    def top_1_song_usa(self) -> str:
        """
        Description:
        ------------
        Get the top 1 song in USA in Spotify

        Return:
        -------
        The name of the top 1 song if the playlist is not empty
        """
        new_playlist = SpotifyHandler()
        new_playlist.init_play_list(
            "https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=4d35ac989d9e4ab2")
        if len(new_playlist.items) != 0:
            return new_playlist.get_songs_name_list()[0]
        else:
            return "The playlist is empty"

    def get_songs_name_list(self) -> list:
        """
        Description:
        ------------
        This method will get the name of every songs in the playlist

        Return:
        -------
        A list of song's names
        """
        song_names = list()
        for i in self.items:
            song_names.append(i["track"]["name"])
        return song_names

    def to_string_genre(self) -> str:
        """
        Description:
        ------------
        Return a list of genre as a string
        """
        genres = ""
        for i in self.get_genres():
            genres += i + " "
        return genres
