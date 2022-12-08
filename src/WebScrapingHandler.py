import pandas as pd
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

    def top_songs_to_dataframe(self, url : str):
        """
         Description:
        ------------
        This method scrapes top artists and songs from a billboard url and returns the information
        in the form of a pandas database.
        Return:
        -------
        A pandas database containing billboard information
        """
        r = requests.get(url)
        songs = []
        artists = []
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('div', class_='o-chart-results-list-row-container')
        for item in items:
            songs.append(item.find('h3').text.strip())
            span_list = item.find_all('span')
            if span_list[1].text.strip() == "NEW":
                artists.append(span_list[3].text.strip())
            elif span_list[1].text.strip() == "RE-\nENTRY":
                artists.append(span_list[3].text.strip())
            else:
                artists.append(span_list[1].text.strip())

        data = {'songs': songs, 'artists': artists}
        df = pd.DataFrame(data)
        return df