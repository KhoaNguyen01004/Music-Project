import SpotifyHandler
import WordCloudHandler
import YouTubeHandler
import CsvHandler

def main():
    sp = SpotifyHandler.SpotifyHandler()
    sp.init_play_list(
        url_link="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33")
    wc = WordCloudHandler.WordCloudHandler(text=sp.to_string_genre())
    wc.wordcloud_to_img('wordcloud.png')
    print(sp.get_most_poplar_genre(sp.get_genres()))


    yt = YouTubeHandler.YouTubeHandler()
    yt.init_playlist()
    print(yt.plot_playlist())

    csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-artists-global-weekly-2022-11-24.csv')
    yt_wc = WordCloudHandler.WordCloudHandler(text= csv.get_artist_with_views(), type = 'freq')
    yt_wc.wordcloud_to_img('YoutubeTopArtist.png')
    

if __name__ == "__main__":
    main()
