from bs4 import BeautifulSoup
import requests
import bs4

def start_scraping():
    url = "http://quotes.toscrape.com/"
    
    # Use requests to get the website
    response = requests.get(url)
    
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get all quotes
    quotes = soup.find_all('div', class_='quote')
    
    print(f"--- Data from {url} ---\n")
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"Quote: {text}")
        print(f"Author: {author}\n")

if __name__ == "__main__":
    start_scraping()
