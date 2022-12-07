import requests
from bs4 import BeautifulSoup


class WebScrapingHandler:

    def most_listened_monthly_spotify(self):
        """
        Description:
        ------------
        This method use to get the most listened monthly based on Wikipedia:
        https://en.wikipedia.org/wiki/List_of_most-streamed_artists_on_Spotify#Most_monthly_listeners

        Return:
        -------
        The artist that is most listened to monthly
        """
        most_monthly_listener = "https://en.wikipedia.org/wiki/List_of_most-streamed_artists_on_Spotify#Most_monthly_listeners"
        page = requests.get(url=most_monthly_listener)
        soup = BeautifulSoup(page.content, "html.parser")
        find = soup.find("div", id="content").find("table").find("a").text
        return find
