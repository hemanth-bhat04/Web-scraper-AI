import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    text = '\n'.join([p.get_text() for p in paragraphs])
    return text

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 10)  # Extract 10 sentences
    return ' '.join(str(sentence) for sentence in summary)

def main():
    url = input("Enter URL to scrape: ")
    
    html = fetch_page(url)
    if html:
        text = extract_text(html)
        print("\nExtracted Text:\n", text)
        summary = summarize_text(text)
        print("\nSummary:\n", summary)
    else:
        print("Failed to fetch page.")

if __name__ == "__main__":
    main()
