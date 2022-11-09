import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "5d2671fe13644512aeb70d497c165c82"
client_secret = "4ae2f73b3aab4106903bc34919f04043"

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

play_list = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33"
items = sp.playlist_tracks(playlist_id=play_list)["items"]

for i in items:
    artist_uri = i['track']['artists'][0]['uri']
    artist_info = sp.artist(artist_uri)
    print(f"{i['track']['name']}, {i['track']['artists'][0]['name']}", end=" ")
    print("(", end="")
    for i in artist_info['genres']:
        if len(artist_info['genres']) > 1:
            print(f"{i}", end=", ")
        else:
            print(f"{i}", end="")
    print(")")
    print("\n")
