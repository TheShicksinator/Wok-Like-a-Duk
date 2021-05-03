import requests as rq
from bs4 import BeautifulSoup


def getResultsTasty(searchTerms):
    searchTerms = searchTerms.lower()
    wordList = searchTerms.split(' ')
    for i in range(len(wordList))[1:]:
        wordList[i] = '%20' + wordList[i]
    page = rq.get('https://tasty.co/search?q=' + ''.join(wordList))
    soup = BeautifulSoup(page.content, 'lxml')
    results = {}
    for element in soup.find_all(class_='feed-item'):
        for tag in element.find_all(class_='feed-item__title'):
            results[tag.text] = element['href']
    return results  # outputs dict in form {title:link}
