import requests
import csv

from bs4 import BeautifulSoup

response = requests.get('http://books.toscrape.com/')

# print(response.status_code)

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)
# h1_tags = soup.find_all('h1')

# for h1_tag in h1_tags:
#     print(h1_tag.text)

# print(h1_tags)

# warnings = soup.find_all('div', class_='alert alert-warning')
# for warning in warnings:
#     print(warning.text)
# print(warnings)

books = soup.find_all('article', class_='product_pod')

# print(books)
data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_="price_color").text
    availability = book.find('p', class_="instock availability").text.strip()
    data.append([title, price, availability])

with open('bookstore.csv', "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])
    writer.writerows(data)



# class="sc-8ea7699c-3 dhclWg"
# class="sc-8ea7699c-3 dhclWg"

# class="sc-b8778340-4 kYtujW"
# class="sc-b8778340-4 kYtujW"


