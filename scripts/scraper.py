import requests as rq
from bs4 import BeautifulSoup


def getIngredientsTasty(site):
    page = rq.get(site)
    # requests site
    soup = BeautifulSoup(page.content, "lxml")
    # parses HTML using lxml parser
    listing = []
    for listItem in soup.find_all(class_="ingredient xs-mb1 xs-mt0"):
        # iterates through elements containing ingredients
        listing.append(listItem.text)
    # print can be subbed for sending to whatever docs are needed. Join will put the list of items into line separated.
    print('\n'.join(listing))
