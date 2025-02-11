import requests
from bs4 import BeautifulSoup
import csv

# initialize the data structure where to
# store the scraped data
products = []

# initialize the list of discovered urls
# with the first page to visit
urls = ["https://www.scrapingcourse.com/ecommerce/"]

# get the page to visit from the list
current_url = urls.pop()

# crawling logic
response = requests.get(current_url)
soup = BeautifulSoup(response.content, "html.parser")

link_elements = soup.select("a[href]")

for link_element in link_elements:
    url = link_element["href"]
    if "https://www.scrapingcourse.com/ecommerce/product" in url:
        urls.append(url)

# until all pages have been visited
while len(urls) != 0:
   
    # get the page to visit from the list
    current_url = urls.pop()  
    
    # if current_url is product page
    if "https://www.scrapingcourse.com/ecommerce/product" in current_url:
        product = {}
        product["url"] = current_url
        product["image"] = soup.select_one(".wp-post-image")["src"]
        product["name"] = soup.select_one(".product_title")
        product["price"] = soup.select_one(".price")

        products.append(product)

# initialize the CSV output file
with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

    # populating the CSV
    for product in products:
        writer.writerow(product.values())
