import SpotifyHandler
import WordCloudHandler


def main():
    sp = SpotifyHandler.SpotifyHandler()
    sp.init_play_list(
        url_link="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33")
    wc = WordCloudHandler.WordCloudHandler(text=sp.to_string_genre())
    wc.wordcloud_to_img()
    print(sp.get_most_poplar_genre(sp.get_genres()))


if __name__ == "__main__":
    main()
