import requests
from bs4 import BeautifulSoup

def scrape_product_price(url):
    # Make a request to the product page
    response = requests.get(url)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    
