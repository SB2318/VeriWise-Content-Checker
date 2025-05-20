from pocketbase import PocketBase
import requests
import fitz
import difflib
from bs4 import BeautifulSoup


class PlagrismService:

    @staticmethod
    def check_plagrism(input_text):
        pb = PocketBase("http://51.20.1.81:8080/")
        pb.admins.auth_with_password("test2345@gmail.com", "test@123") # GLOBAL USER AS OF NOW
        records = pb.collection("content").get_full_list(200) # GET ALL CONTENTS FROM DB

        # Iterate through each record and compare content
        for record in records:
         # Determine the content source
         content = None
         if record.body:
            content = record.body
         elif record.html_file:
            content = PlagrismService().extract_html_file_content(record.html_file, record.id, 'content')
         elif record.html_content:
            content = PlagrismService().extract_html_content(record.html_content)
         elif record.pdf_file:
            content = PlagrismService().extract_pdf_file_content(record.pdf_file, record.id, 'content')
         elif record.source_url:
            content = PlagrismService().extract_source_url_content(record.source_url)
        
         plagiarised_matches = []
         if content:
            similarity = difflib.SequenceMatcher(None, input_text, content).ratio()
            if similarity > 0.8:  
                plagiarised_matches.append({
                    "title": record.get("title"),
                    "similarity": similarity,
                    "matching_text": content
                })
        if plagiarised_matches:
          best_match = max(plagiarised_matches, key=lambda x: x['similarity'])
          return {
            "plagiarised_percentage": round(best_match["similarity"] * 100, 2),
            "plagiarised_text": best_match["matching_text"],
            "source_title": best_match["title"]
          }
        else:
           return {
            "plagiarised_percentage": 0,
            "plagiarised_text": "",
            "source_title": ""
          }

    @staticmethod
    def extract_html_file_content(file_name, record_id, collection_name):
         try:
           file_url = f"http://51.20.1.81:8080/api/files/{collection_name}/{record_id}/{file_name}"
           response = requests.get(file_url, stream=True)
           response.raise_for_status()
           soup = BeautifulSoup(response.text, 'html.parser')
           text = soup.get_text(separator=' ', strip=True)

           return text

         except Exception as e:
             print(f"Error extracting HTML file content: {e}")
             return ""
   
    @staticmethod
    def extract_html_content(html_content):
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        return text

    @staticmethod
    def extract_pdf_file_content(file_name, record_id, collection_name):
          try:
            file_url = f"http://51.20.1.81:8080/api/files/{collection_name}/{record_id}/{file_name}"
            response = requests.get(file_url, stream=True)
            response.raise_for_status()
        
            # pdf
            pdf_doc = fitz.open(stream=response.content, filetype="pdf")

            text = ""
            for page in pdf_doc:
             text += page.get_text()

            pdf_doc.close()

            return text.strip() 

          except Exception as e:
             print(f"Error extracting HTML file content: {e}")
             return ""
   
    @staticmethod
    def extract_source_url_content(url):
          try:
        
           response = requests.get(url, stream=True)
           response.raise_for_status()
           soup = BeautifulSoup(response.text, 'html.parser')
           text = soup.get_text(separator=' ', strip=True)

           return text

          except Exception as e:
             print(f"Error extracting HTML file content: {e}")
             return ""
   
       
       
        
       


       
         

