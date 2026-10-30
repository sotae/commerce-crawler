import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"
books = []

while True:
    res = requests.get(url, timeout=10)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        books.append((title, price))

    next_btn = soup.select_one("li.next a")
    if next_btn is None:
        break
    
    print(next_btn["href"])
    url = urljoin(url, next_btn["href"])
    time.sleep(1)

print(len(books))