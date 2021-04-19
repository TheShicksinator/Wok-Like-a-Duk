import requests as rq
from bs4 import BeautifulSoup
page = rq.get('https://tasty.co/recipe/hainanese-chicken-rice')
# requests site
soup = BeautifulSoup(page.content, "lxml")
# parses HTML using lxml parser

for listItem in soup.find_all(class_="ingredient xs-mb1 xs-mt0"):
    # iterates through elements containing ingredients
    listing = listItem.text
    print(listing)
