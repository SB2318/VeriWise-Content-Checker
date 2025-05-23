from pocketbase import PocketBase
import requests
import fitz

from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from cachetools import TTLCache, cached

# 12 hour in sec
pocketbase_cache = TTLCache(maxsize=1, ttl=43200)

@cached(pocketbase_cache)
def get_all_pocketbase_content():
    pb = PocketBase("http://51.20.1.81:8080/")
    pb.admins.auth_with_password("test2345@gmail.com", "test@123")
    return pb.collection("content").get_full_list(200)

class PlagiarismService:

    @staticmethod
    def check_plagiarism(input_text):
      
        records = get_all_pocketbase_content()

        contents = []
        titles = []

        # Iterate through each record and compare content
        for record in records:
         # Determine the content source
         content = None
         if record.body:
            content = record.body
         elif record.html_file:
            content = PlagiarismService().extract_html_file_content(record.html_file, record.id, 'content')
         elif record.html_content:
            content = PlagiarismService().extract_html_content(record.html_content)
         elif record.pdf_file:
            content = PlagiarismService().extract_pdf_file_content(record.pdf_file, record.id, 'content')
         elif record.source_url:
            content = PlagiarismService().extract_source_url_content(record.source_url)
        
         
         if content:
           contents.append(content)
         if record.title:
           titles.append(record.title)
        
        if not contents:
           return {
            "plagiarised_percentage": 0,
            "plagiarised_text": "",
            "source_title": ""
          }
        # check plagiarism using TF-DF and cosine similarity
        
        documents = contents + [input_text]

        # TF-DF Vectorization
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents).toarray()
        # cosine similarity with all exitisting content
        cosine_similarities = cosine_similarity([vectors[-1]], vectors[:-1])[0]
        # Find best match
        max_index = cosine_similarities.argmax()
        max_score = cosine_similarities[max_index]

        if max_score > 0.8:
           return {
            "plagiarised_percentage": round(max_score*100, 2),
            "plagiarised_text": contents[max_index],
            "source_title": titles[max_index]
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
   
       
       
        
### Detailed explanation

### We are collecting all existing contents from our pocketbase datasource
### Based on the content type we are extracting those content
### We are using BeautifulSoup to parse the HTML content and extract the text
### We are using fitz to extract the text from the PDF content


### Here, I am using TF-IDF and cosine similarity to check  the similarity between the content of the source and the content of the pocketbase datasource
### If the similarity is above 0.8, we are returning, Yes Plagiarism found

### To achieve our goal I am  using an NLP tool, named TfidfVectorizer to convert text into numbers.
### Then I am using cosine_similarity to calculate the similarity between the two vectors.

### TF-IDF stands for Term Frequency-Inverse Document Frequency.

### One thing is to notice, we are using cosine similarity to compare the input text vector with all the other document vectors.
### vectors[-1] means input_text, since it added at the last
### vectors[:-1] means all other documents, since we are excluding the last one
### This gives you list of scores between 0 and 1
### We are returning the index of the document with the highest similarity score


       
         

