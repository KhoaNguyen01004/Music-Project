import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "e92db17472c34f5294229fdb3cf08ccb"
client_secret = "88e6b43105cb448290290f0e837d0f90"

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

play_list = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1rVRqp?si=e20f8b3bd52c4427"
items = sp.playlist_items(playlist_id=play_list)["items"]

for i in items:
    print(i)
    break

