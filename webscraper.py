
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
   
    soup = BeautifulSoup(response.content, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    
    # Extract and print the title and price for each book
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").get_text()
        print(f"Title: {title}, Price: {price}")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
