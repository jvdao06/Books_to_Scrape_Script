# Books_to_Scrape_Script

# Objective: Write a program to collect book information from http://books.toscrape.com/ 

1. Scrape product description and all product info for all books in the Science and Poetry categories.

2. Save results to a database (Database of your choice, text/excel file is fine, but SQL is preferred)

# Requirements

beautifulsoup4==4.10.0

certifi==2021.10.8

charset-normalizer==2.0.7

idna==3.2

integer==1.0.3

numpy==1.21.2

pandas==1.3.4

python-dateutil==2.8.2

pytz==2021.3

requests==2.26.0

six==1.16.0

soupsieve==2.2.1

urllib3==1.26.7

# Instructions:

Initial Steps:

Run $ pip install -r requirements.txt in command to install all packages necessary for the function.

1.Run the book_to_scrape_script.py to run the scraping function on specified Genres
    - You can define which Genres to scrape by the URLS:
    eg. https://books.toscrape.com/catalogue/category/books/travel_2/index.html = Travel

2. Scraping Function will then collect all the books listed in each genre and scape the production information data

3. Function will create output csv based on each Genre and data scraped.

