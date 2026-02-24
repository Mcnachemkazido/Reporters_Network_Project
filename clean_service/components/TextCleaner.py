import string



class TextCleaner:
    def __init__(self, logger):
        self.logger = logger

    def clean(self,text):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        self.logger.info('I did a basic cleaning the text')
        return clean_text


