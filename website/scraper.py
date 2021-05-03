import requests as rq
from bs4 import BeautifulSoup
from flask import Flask


def getTitleTasty(site):
    page = rq.get(site)
    soup = BeautifulSoup(page.content, 'lxml')
    result = (soup.title).text
    return result


def getIngredientsTasty(site):
    page = rq.get(site)
    # requests site
    soup = BeautifulSoup(page.content, "lxml")
    # parses HTML using lxml parser
    listing = []
    for listItem in soup.find_all(class_="ingredient xs-mb1 xs-mt0"):
        # iterates through elements containing ingredients
        listing.append(listItem.text)
    return listing  # list of ingredients


def getInstructionsTasty(site):
    page = rq.get(site)
    # requests site
    soup = BeautifulSoup(page.content, "lxml")
    # parses HTML using lxml parser
    listing = []
    for listItem in soup.find_all('li', class_="xs-mb2"):
        # iterates through elements containing ingredients
        listing.append(listItem.text)
    return listing  # list of instructions
