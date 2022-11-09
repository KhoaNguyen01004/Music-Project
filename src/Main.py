import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "5d2671fe13644512aeb70d497c165c82"
client_secret = "4ae2f73b3aab4106903bc34919f04043"

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

play_list = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1rVRqp?si=e20f8b3bd52c4427"
items = sp.playlist_tracks(playlist_id=play_list)["items"]

for i in items:
    artist_info = i["track"]
    print(f"{i['track']['name']}, {artist_info['artists'][0]['name']}")
