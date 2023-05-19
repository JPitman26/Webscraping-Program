# Webscraping-Program

- [Webscraping-Program](#webscraping-program)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Notes](#notes)
  - [License](#license)

## Introduction

This Python script scrapes the price of a specific product from the website. It utilizes the BeautifulSoup library for parsing HTML and the Requests library for making HTTP requests.

## Features

- Sends an HTTP request to the website and retrieves the product page.
- Parses the HTML response using BeautifulSoup to locate the price element.
- Extracts and displays the price of the product.

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- beautifulsoup4 library (`pip install beautifulsoup4`)

## Usage

1. Clone the repository.
    ```bash
   git clone https://github.com/JPitman26/Webscraping-Program.git
2. Navigate to the project directory.
      ```bash
   cd webscraping-program
3. Modify the `product_url` variable in `app.py` to the desired product URL.
4. Run the script.
     ```bash
   python app.py
5. The program will output the price of the product on the console.

## Notes

- Ensure that you have a stable internet connection for successful HTTP requests.
- Respect the website's terms of service and scraping guidelines.
- This script is provided as a demonstration of web scraping concepts and should be used responsibly.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.


