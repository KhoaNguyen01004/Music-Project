import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

    #
    #    Converts pandas database of billboard rankings into a text file
    #
def top_200_to_text(df):
    billboard_artists = str()
    for artists in df['artists']:
        billboard_artists += artists.replace(' ', '-') + "\n"
    print(billboard_artists)
    return billboard_artists

#  Returns database showing number of songs each artist had on billboard charts

def number_of_songs_artist_has(df):
    dups = df.pivot_table(index=['artists'], aggfunc='size')
    return dups.sort_values(ascending=False)


    # Compares whether or not the top radio song and the top streamed song on billboard are the same
def compare_streams_to_radio():
    r = requests.get('https://www.billboard.com/charts/streaming-songs/')
    soup = BeautifulSoup(r.content, 'html.parser')
    stream_song = soup.find('a', class_='c-title__link lrv-a-unstyle-link').text.strip()
    r2 = requests.get('https://www.billboard.com/charts/radio-songs/#')
    soup2 = BeautifulSoup(r2.content, 'html.parser')
    radio_song = soup2.find('a', class_='c-title__link lrv-a-unstyle-link').text.strip()
    if stream_song == radio_song:
        print("The top streamed song and the top song played on the radio are the same!")
        print("It's " + stream_song)
    else:
        print("The top streamed song and the top song played on the radio are different!")
        print("The top streamed song is, " + stream_song + ", and the top song played on the radio is, " + radio_song)