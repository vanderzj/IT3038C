# Imports requests to get webdata and BeautifulSoup to be able to scrape through that data.
from bs4 import BeautifulSoup
import requests

# Gets the html of the chosed website and creates a BeautifulSoup object to parse it with.
data = requests.get('https://www.iam8bit.com/collections/the-pathless/products/the-pathless-2xlp').content
soup = BeautifulSoup(data, "lxml")

# Gets the price of the product and removes all line breaks and spaces.
tag = soup.find("div", {"class":"price"}).text
price = tag.replace("\n","")
price2 = price.replace(" ", "")

# Gets the title of the product and removes all line breaks and spaces. 
# (Note: Not the cleanest way to do it but this site uses a lot of spaces to position their text.)
tag2 = soup.find("div", {"class":"product-name top-product-detail"}).text
title = tag2.replace("\n","")
title2 = title.replace(" ", "")

# Formats the product title and price into a readable line.
print("%s costs %s." % (title2, price2))