import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def fetch_text(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return "\n".join([p.get_text() for p in paragraphs])
    return None

def extract_info(text, query):
    model_name = "google/flan-t5-large"  # Free model from Hugging Face
    nlp = pipeline("question-answering", model=model_name)
    response = nlp(question=query, context=text)
    return response['answer']

url = input("Enter URL: ")
query = input("Enter what you want to extract: ")

text = fetch_text(url)
if text:
    extracted_info = extract_info(text, query)
    print("\nExtracted Information:\n", extracted_info)
else:
    print("Failed to fetch page.")
