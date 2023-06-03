import requests
from bs4 import BeautifulSoup
import csv
import time

books = []

for i in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        starTag = article.find('p')
        star = starTag['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, star, price])

    time.sleep(15)  

filename = 'books.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Star Rating', 'Price'])
    writer.writerows(books)

print('Data saved to', filename)
