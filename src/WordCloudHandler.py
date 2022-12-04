import wordcloud


class WordCloudHandler:

    wc = wordcloud.WordCloud(stopwords=wordcloud.STOPWORDS)

    def __init__(self, text, type: str = 'normal') -> wordcloud:
        """
        Description:
        ------------
        If type is 'normal' then generate based off of how frequent the word appears within the text.
        If type is 'freq' then generate based off of a frequency specified by a value.
        Default is 'normal'.
        """
        if type == 'normal':
            self.wc.generate(text=text)
        elif type == 'freq':
            self.wc.generate_from_frequencies(text)

    def wordcloud_to_img(self, filename: str = 'wordcloud.png'):
        """
        Description:
        ------------
        Saves the wordcloud as an image with the specified file name.
        Default is 'wordcloud.png'.
        """
        filename = '{}/{}'.format('img', filename)
        self.wc.to_file(filename = filename)

    def add_stop_word(self, word: str):
        """
        Description:
        ------------
        This will add a stop word to a list if it not yet in stop word list
        """
        wordcloud.STOPWORDS.add(word)