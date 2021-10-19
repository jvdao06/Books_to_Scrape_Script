import requests
import re
import pandas as pd

from bs4 import BeautifulSoup


def scrape_from_url(url):
    # Generate Request Payloads from Url to specific Genres
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    books_in_genre = []
    for x in soup.findAll("article", class_="product_pod"):
        # Generating links for each book in specified genre
        books_in_genre.append("https://books.toscrape.com/catalogue/" + x.div.a.get('href').replace("../../../", ""))

    print(f"Pulling Book information from Genre Page", books_in_genre)

    production_information_table_final_df = pd.DataFrame()
    production_information_table_value = []
    # Generating Genre Payload from each book in specified Genre
    for obj in books_in_genre:

        print(f"Scraping from Page", obj)
        response_get = requests.get(obj)
        book_hyperlink = BeautifulSoup(response_get.text, 'html.parser')
        print(f"----------------------------")
        for bookinfo in book_hyperlink.findAll("div", class_="content"):
            # Append Title
            production_information_table_value.append(bookinfo.find("h1").text)
            # Append Production Rating
            production_information_table_value.append(
                bookinfo.find("p", class_=re.compile("star-rating")).get("class")[1])
            # Append Production Desciption
            production_information_table_value.append(bookinfo.find("p", class_="").text)
            # Scraping Production Information Table
            for tr in bookinfo.findAll('tr'):
                pd_value = tr.find('td').text

                production_information_table_value.append(pd_value)
            # Formatting Payload into consumable format
            production_information_table_df = pd.DataFrame(production_information_table_value)

            production_information_table_df_transpose = production_information_table_df.T

            production_information_table_df_transpose.columns = ["Title",
                                                                 "Rating",
                                                                 "Description",
                                                                 "UPC",
                                                                 "Product Type",
                                                                 "Price Excl Tax",
                                                                 "Price Incl Tax",
                                                                 " Tax",
                                                                 "Availability",
                                                                 "Number Of Reviews"]

            production_information_table_value = []
            # Creating Finalized Payload for specified Genre
            production_information_table_final_df = production_information_table_final_df.append(
                production_information_table_df_transpose)

    return production_information_table_final_df


def main():

    # Function currently scrapes based on the URL to a specific Genre page
    # Input Parameters for each URL
    url_links = ["https://books.toscrape.com/catalogue/category/books/science_22/index.html",
                 "https://books.toscrape.com/catalogue/category/books/poetry_23/index.html"]

    print(f"----------------------------")

    # Iterate over each URL for specified Genre and call scraper function
    for x in url_links:
        genre_data_payload = pd.DataFrame(scrape_from_url(x))
        print(f"----------------------------")

        genre_name = re.search('books/(.+?)/index.html', x).group(1)
        print(f"Creating file "+ genre_name+".csv")
        filename = genre_name+".csv"
        print(f"----------------------------")

        genre_data_payload.to_csv(filename, index=False)
        print(f"Running Scraping Function on link and creating file for ", genre_data_payload)


main()