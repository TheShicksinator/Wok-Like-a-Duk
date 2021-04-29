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
    with open('ingredients.txt', 'w') as file:
        for line in listing:
            line.encode('utf-8')
            file.write(line + "\n")
    # TODO: Fix encoding of special characters

    # print('\n'.join(listing))
