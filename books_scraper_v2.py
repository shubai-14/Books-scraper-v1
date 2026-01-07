import requests
import csv
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

books_data = []
page_number = 1

session = requests.Session()

base_url = "https://books.toscrape.com/"
url = base_url

rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

while url:
    print(f"Scraping page: {page_number}")
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")
        
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            stock = book.find("p", class_="instock availability").text.strip()

            rating_classes = book.find("p", "star-rating")
            rating_class = rating_classes["class"]
            rating_text = rating_class[1]
            rating = rating_dict.get(rating_text, 0)

            img_url = book.find("img")["src"]
            img_url = urljoin(base_url, img_url)

            book_url = book.a["href"]
            book_url = urljoin(base_url, book_url)

            

            books_data.append([
                title,
                price,
                stock,
                rating,
                img_url,
                book_url




            ])

            print(f"Total books scraped so far {len(books_data)}")

        next_button = soup.find("li", class_="next")
        if next_button:
            url = urljoin(url, next_button.a["href"])
            page_number += 1
        else:
            url = None


    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

    except Exception as e:

        print(f"Something went wrong on page {page_number}: {e}")

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Stock", "Rating", "IMG_Url", "BookURL"])
    writer.writerows(books_data)

print(f"CSV Successfully created")

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books_data, f, indent=4, ensure_ascii=False)

print(f"Json Succesfully created")

