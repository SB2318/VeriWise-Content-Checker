
# The service will only help you to detect any watermark, logo, text with copyright symbol present
# in the image. It will not remove the watermark or logo from the image.
import cv2
import pytesseract 
from pytesseract import Output
from app.utils.copyright_utils import restricted_keywords

class CopyrightCheckerService:
   @staticmethod
   def detect_copyrighted_text(image_path):
       # load image
       image = cv2.imread(image_path)
       # convert image to grayscale
       gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       #Improve text detection
       gray = cv2.GaussianBlur(gray, (3,3), 0)
       # perform OCR on the image
       data = pytesseract.image_to_data(gray, output_type=Output.DICT)

       # Define some predefine keyword and try to find the match
       detected_keywords = []
       for i, text in enumerate(data['text']):
        if any(k.lower() in text.lower() for k in restricted_keywords):
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            detected_keywords.append(text)
            if detected_keywords:
               return {
                "copyrighted_content": detected_keywords,
                "copyright_found": True
                }
       
       if detected_keywords:
            return {
                "copyrighted_content": detected_keywords,
                "copyright_found": True
            }
        else:
            return {
                "detected_keywords": [],
                "copyright_exist": False
            }
       
    