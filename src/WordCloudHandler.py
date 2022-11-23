import wordcloud


class WordCloudHandler:

    wc = wordcloud.WordCloud(stopwords=wordcloud.STOPWORDS)

    def __init__(self, text: str) -> wordcloud:
        self.wc.generate(text=text)

    def wordcloud_to_img(self):
        self.wc.to_file(filename="wordcloud.png")

    def add_stop_word(self, word: str):
        wordcloud.STOPWORDS.add(word)