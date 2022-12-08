import SpotifyHandler
import WordCloudHandler
import YouTubeHandler
import CsvHandler
import MenuHandler
import os
import BarGraph
import Spotify_Popularity
import MatPlotLibHandler
import WebScrapingHandler
import BillboardHandler


def main():
    # sp = SpotifyHandler.SpotifyHandler()
    # sp.init_play_list(
    #     url_link="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33")
    # wc = WordCloudHandler.WordCloudHandler(text=sp.to_string_genre(), type="normal")
    # wc.wordcloud_to_img('wordcloud.png')
    # print(sp.get_most_poplar_genre(sp.get_genres()))

    # yt = YouTubeHandler.YouTubeHandler()
    # yt.init_playlist()
    # print(yt.plot_playlist())

    # csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-artists-global-weekly-2022-11-24.csv')
    # yt_wc = WordCloudHandler.WordCloudHandler(text= csv.get_artist_with_views(), type = 'freq')
    # yt_wc.wordcloud_to_img('YoutubeTopArtist.png')

    sp = SpotifyHandler.SpotifyHandler()
    sp.init_play_list(
        url_link="https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=30a40fcfc3a74d33")

    yt = YouTubeHandler.YouTubeHandler()
    yt.init_playlist()

    again = True  # Determine if the program will continue running or not
    menu = MenuHandler.MenuHandler().default_menu()
    ws = WebScrapingHandler.WebScrapingHandler()
    mp = MatPlotLibHandler.MatPlotLibHandler()

    while (again):
        menu.show_menu()
        user = input("Please select your option: ")
        user = menu.valid_user_input(user=user)
        option = int(user)
        if option == 1:
            wc = WordCloudHandler.WordCloudHandler(sp.to_string_genre())
            wc.wordcloud_to_img(filename="MostPopularGenreWC.png")
            wc.show_wordcloud_img()
            print(
                f"The most popular genre globally on Spotify is {sp.get_most_poplar_genre()}")
            os.system("pause")
        if option == 2:
            print(f"Top 1 song in USA is {sp.top_1_song_usa()}")
            os.system("pause")
        if option == 3:
            print(
                f"{ws.most_listened_monthly_spotify()} is the most listened artist on Spotify according to Wikipedia")
            os.system("pause")
        if option == 4:
            yt_ta_csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-artists-global-weekly-2022-11-24.csv')
            yt_wc = WordCloudHandler.WordCloudHandler(text= yt_ta_csv.get_artist_with_views(), type = 'freq')
            yt_wc.wordcloud_to_img('YoutubeTopArtist.png')
            yt_wc.show_wordcloud_img('img\YoutubeTopArtist.png')
            os.system("pause")
        if option == 5:
            yt_x_label = 'Video Title'
            yt_y_label = 'View Count (in hundred millions)'
            mp.plot('Trending Songs In US On Youtube.png', yt.get_titles(), yt.get_views(), 'Current Popular Songs on YouTube and Their View Counts', yt_x_label, \
            yt_y_label)
            os.system("pause")
        if option == 6:
            yt_x_label = 'Video Title'
            yt_y_label = 'View Count (in hundred millions)'
            ytca_csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-songs-ca-weekly-2022-12-01.csv')
            ytus_csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-songs-us-weekly-2022-12-01.csv')
            mp.plot_two('Canada and U.S. Comparison of Top Songs on Youtube.png', ytca_csv.get_track_names(), ytca_csv.get_views(), ytus_csv.get_track_names(), \
            ytus_csv.get_views(), ['Canada', 'United States'], 'Comparison of Top Songs on Youtube Canada Vs. United States', yt_x_label, yt_y_label)
            os.system("pause")
        if option == 7:
            df = ws.top_songs_to_dataframe('https://www.billboard.com/charts/billboard-global-200/')
            BillboardHandler.top_200_to_text(df)
            wc2 = WordCloudHandler.WordCloudHandler('billboard_artists.txt')
            wc2.wordcloud_to_img(filename="TopBillboardArtists.png")
            wc2.show_wordcloud_img("img/TopBillboardArtists.png")
            os.system("pause")
        if option == 8:
            df = ws.top_songs_to_dataframe('https://www.billboard.com/charts/billboard-global-200/')
            dups = BillboardHandler.number_of_songs_artist_has(df)
            graph = BarGraph.BarGraph()
            graph.init_Creat_BarGraph(dups.index, dups, 'Artist Song Counts')
            wc = WordCloudHandler.WordCloudHandler("test")
            wc.show_wordcloud_img("img/Artist Song Counts.png")
            os.system("pause")
        if option == 9:
            BillboardHandler.compare_streams_to_radio()
            os.system("pause")
        if option == 10:
            Sopt_Pop = Spotify_Popularity.SpotifyPopularity()
            artist_Popularity_US = Sopt_Pop.get_Artist_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
            bg = BarGraph.BarGraph()
            bg.init_Creat_BarGraph(artist_Popularity_US['Artist Name'],artist_Popularity_US['Artist Popularity'],'Artists', "Artist Popularity Top 50 US")
            os.system("pause")
        if option == 11:
            Sopt_Pop = Spotify_Popularity.SpotifyPopularity()
            track_PopularityUS = Sopt_Pop.get_Track_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
            bg = BarGraph.BarGraph()
            bg.init_Creat_BarGraph(track_PopularityUS['Track Name'],track_PopularityUS['Track Popularity'],'Tracks' ,"Track Popularity Top 50 US")
            os.system("pause")
        if option == 12:
            Sopt_Pop = Spotify_Popularity.SpotifyPopularity()
            bg = BarGraph.BarGraph()
            artist_Popularity_France = Sopt_Pop.get_Artist_Pop('https://open.spotify.com/playlist/37i9dQZEVXbIPWwFssbupI')
            bg.init_Creat_BarGraph(artist_Popularity_France['Artist Name'],artist_Popularity_France['Artist Popularity'],'Artists', "Artist Popularity Top 50 in France")

            artist_Popularity_Spain = Sopt_Pop.get_Artist_Pop('https://open.spotify.com/playlist/37i9dQZEVXbNFJfN1Vw8d9')
            bg.init_Creat_BarGraph(artist_Popularity_Spain['Artist Name'],artist_Popularity_Spain['Artist Popularity'],'Artists',"Artist Popularity Top 50 in Sapin")
            os.system("pause")
        # TODO add more option and what should they do each case make sure to pause the program each case
        else:
            if option == len(menu.menu) - 1:
                menu.print_help()
            elif option == len(menu.menu):
                print("Thank you for using")
                os.system("pause")
                again = False

    # wc = WordCloudHandler.WordCloudHandler(text=sp.to_string_genre(), type="normal")
    # wc.wordcloud_to_img('wordcloud.png')

    # mp = MatPlotLibHandler.MatPlotLibHandler()
    # yt = YouTubeHandler.YouTubeHandler()
    # yt.init_playlist()
    # yt_x_label = 'Video Title'
    # yt_y_label = 'View Count (in hundred millions)'
    # mp.plot('Trending Songs In US On Youtube.png', yt.get_titles(), yt.get_views(), 'Current Popular Songs on YouTube and Their View Counts', yt_x_label, \
    #   yt_y_label)

    # csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-artists-global-weekly-2022-11-24.csv')
    # yt_wc = WordCloudHandler.WordCloudHandler(text= csv.get_artist_with_views(), type = 'freq')
    # yt_wc.wordcloud_to_img('Youtube Top Artist.png')

    # ytca_csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-songs-ca-weekly-2022-12-01.csv')
    # ytus_csv = CsvHandler.CsvHandler(file_name = 'youtube-charts-top-songs-us-weekly-2022-12-01.csv')
    # mp.plot_two('Canada and U.S. Comparison of Top Songs on Youtube.png', ytca_csv.get_track_names(), ytca_csv.get_views(), ytus_csv.get_track_names(), \
    #    ytus_csv.get_views(), ['Canada', 'United States'], 'Comparison of Top Songs on Youtube Canada Vs. United States', yt_x_label, yt_y_label)

    # Sopt_Pop = Spotify_Popularity.SpotifyPopularity()
    # populatery_US = Sopt_Pop.get_Artist_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
    # track_PopularityUS = Sopt_Pop.get_Track_Pop("https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp")
    # bg = BarGraph.BarGraph()
    # bg.init_Creat_BarGraph(populatery_US['Artist Name'],populatery_US['Artist Popularity'],"Artist Popularity")
    # bg.init_Creat_BarGraph(track_PopularityUS['Track Name'],track_PopularityUS['Track Popularity'],"Track Popularity")


if __name__ == "__main__":
    main()
