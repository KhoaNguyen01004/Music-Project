import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from SpotifyHandler import SpotifyHandler


class SpotifyPopularity(SpotifyHandler):

    client_ID = '4b80f75a5f2b4ef0a25401d01d9e8bb2'
    client_Secret = 'ad2ee9e8bcdf449c94d6151f96774bf1'
    # Authentication - without user
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_ID, client_secret=client_Secret)
    sp = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager)

    def get_Artist_Pop(self, URL):
        A_name = []
        A_Pop = []
        playlist_URI = URL.split("/")[-1].split("?")[0]
        for track in self.sp.playlist_tracks(playlist_URI)["items"]:
            # Main Artist
            artist_uri = track["track"]["artists"][0]["uri"]
            artist_info = self.sp.artist(artist_uri)

            #Name, popularity, genre
            artist_name = track["track"]["artists"][0]["name"]
            artist_pop = artist_info["popularity"]

            A_name.append(artist_name)
            A_Pop.append(artist_pop)
        dict_Aritsit = {'Artist Name': A_name,
                        'Artist Popularity': A_Pop}
        return dict_Aritsit

    def get_Track_Pop(self, URL):
        t_Name = []
        t_Pop = []
        playlist_URI = URL.split("/")[-1].split("?")[0]
        for track in self.sp.playlist_tracks(playlist_URI)["items"]:

            # Track name
            track_name = track["track"]["name"]
            t_Name.append(track_name)

            # Popularity of the track
            track_pop = track["track"]["popularity"]
            t_Pop.append(track_pop)
        dict_Track = {'Track Name': t_Name,
                      'Track Popularity': t_Pop}
        return dict_Track
