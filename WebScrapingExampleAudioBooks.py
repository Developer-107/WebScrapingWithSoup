import csv
import requests
from bs4 import BeautifulSoup

# Preparing headers for request
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)   Gecko/20100101 Firefox/78.0"}

# Empty lists for each of the values we want to fetch
titles = []
authors = []
price = []

# Looping through pages
for page in range (1,4):
    response = requests.get(f"|HEREWASURL|{page}", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Scraping title data
    title_data = soup.find_all('h3', attrs={"class":"bc-heading bc-color-link bc-pub-break-word bc-size-medium"})

    # Scraping author data
    author_data = soup.find_all('li', attrs={"class":"bc-list-item authorLabel"})

    # Scraping price data
    price_data = soup.find_all('span', attrs={"class": "bc-text bc-size-base bc-color-base"})

    # Fetching data
    for num in range (0, 40):
        titles.append(title_data[num].text.strip())
        authors.append(author_data[num].text.strip().split("\n")[1].strip())

    for num in range(0, 120):
        price.append(price_data[num].text.strip())

# Cleaning price data
price = price[1:len(price) + 1:3]

all_books_data = []

# Merging each book title with its author's name and price
for num in range(0, 120):
    data = {
        "title" : f"{titles[num]}",
        "author": f"{authors[num]}",
        "price": f"{price[num]}"
        }
    all_books_data.append(data)

# Writing in csv
with open('scraped_books_record.csv', 'w', newline='') as csvfile:
    fieldnames = ["title", "author", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_books_data)
# That's all don't forget to take in mind that each website has its own html so they have to be fetched individually