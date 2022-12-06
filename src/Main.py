import SpotifyHandler
import WordCloudHandler
import YouTubeHandler
import CsvHandler
import MenuHandler
import os

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

    again = True #Determine if the program will continue running or not
    menu = MenuHandler.MenuHandler().default_menu()

    while(again):
        menu.show_menu()
        user = input("Please select your option: ")
        user = menu.valid_user_input(user=user)
        option = int(user)
        if option == 1:
            print(sp.get_most_poplar_genre())
            os.system("pause")
        #TODO add more option and what should they do each case make sure to pause the program each case
        else:
            if option == len(menu.menu) - 1:
                menu.print_help()
            elif option == len(menu.menu):
                again = False
            
    



if __name__ == "__main__":
    main()
