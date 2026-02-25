import easyocr



class OCREngine:
    def __init__(self, logger):
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.logger = logger


    def extract_text(self,image_path):
        extract_info = self.reader.readtext(image_path, detail=0)
        self.logger.info(f'i extract_info for image ,image_path: {image_path}')
        return extract_info




