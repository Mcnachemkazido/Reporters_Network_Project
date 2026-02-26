import heapq
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')



class TextAnalyzer:
    def __init__(self,logger):
        self.logger = logger
        self.weapons_list = self.init_weapons()


    def init_weapons(self):
        with open('weapons/weapons.txt', 'r') as f:
            self.logger.info('I brought the weapons page into the system.')
            return [line.rstrip() for line in f]



    def ten_words(self,text):
        text = text.split()
        f = {}
        for word in text:
            f[word] = f.get(word, 0) + 1
        top10_keys = [k for k, _ in heapq.nlargest(10, f.items(), key=lambda kv: kv[1])]
        self.logger.info('2️⃣I analyzed the 10 most common words')
        return top10_keys


    def get_weapons(self,text):
        weapons_list = self.weapons_list
        weapons = []
        for i in weapons_list:
            if i in text:
                weapons.append(i)
        self.logger.info('3️⃣I performed a text search for weapons.')
        if weapons:
            return weapons
        return None


    def analyzing_emotion_text(self,text):
        res = SentimentIntensityAnalyzer().polarity_scores(text)
        self.logger.info('4️⃣I analyzed the emotions of the text.')
        if res['compound'] < -0.4999:
            return 'negative'
        elif res['compound'] >= 0.5000:
            return 'positive'
        else:
            return 'neutral'

    def analysis_flow(self,text):
        data_analysis = {
            'ten_words': self.ten_words(text),
            'weapons': self.get_weapons(text),
            'emotion_text': self.analyzing_emotion_text(text)}
        return data_analysis



