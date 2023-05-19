import requests
from bs4 import BeautifulSoup

def scrape_product_price(url):
    # Make a request to the product page
    response = requests.get(url)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the element containing the price
    price_element = soup.find("div", class_="product-price")
    if price_element:
        price = price_element.text.strip()
        return price
    else:
        return "Price not found."

# Example usage
product_url = "example-product.com"
price = scrape_product_price(product_url)
print("Price:", price)
