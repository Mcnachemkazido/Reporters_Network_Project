import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt_tab')
stop_words = set(stopwords.words('english'))

class TextCleaner:
    def __init__(self, logger):
        self.logger = logger

    def basic_clean(self,text):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        self.logger.info('I did a basic cleaning the text')
        return clean_text

    def clean_stop_words(self,text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word not in stop_words]
        self.logger.info('I did a stop words cleaning the text')
        return " ".join(filtered_tokens)


    def cleaning_process(self,text):
        stop_a = self.basic_clean(text)
        stop_b = self.clean_stop_words(stop_a)
        return stop_b









