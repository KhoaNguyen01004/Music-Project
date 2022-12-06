import SpotifyHandler
import WordCloudHandler
import YouTubeHandler
import CsvHandler
import BarGraph
import Spotify_Popularity

def main():
    sp = SpotifyHandler.SpotifyHandler()
    sp.init_play_list(
        url_link="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33")
    wc = WordCloudHandler.WordCloudHandler(text=sp.to_string_genre(), type="normal")
    wc.wordcloud_to_img('wordcloud.png')
    print(sp.get_most_poplar_genre(sp.get_genres()))


    yt = YouTubeHandler.YouTubeHandler()
    yt.init_playlist()
    print(yt.plot_playlist())

    csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-artists-global-weekly-2022-11-24.csv')
    yt_wc = WordCloudHandler.WordCloudHandler(text= csv.get_artist_with_views(), type = 'freq')
    yt_wc.wordcloud_to_img('YoutubeTopArtist.png')
    
    Sopt_Pop = Spotify_Popularity.SpotifyPopularity()
    populatery_US = Sopt_Pop.get_Artist_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
    track_PopularityUS = Sopt_Pop.get_Track_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
    bg = BarGraph.BarGraph()
    bg.init_Creat_BarGraph(populatery_US['Artist Name'],populatery_US['Artist Popularity'],"Artist Popularity")
    bg.init_Creat_BarGraph(track_PopularityUS['Track Name'],track_PopularityUS['Track Popularity'],"Track Popularity")


if __name__ == "__main__":
    main()
