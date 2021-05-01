import requests as rq
from bs4 import BeautifulSoup


def getResultsTasty(searchTerms):
    searchTerms = searchTerms.lower()
    wordList = searchTerms.split(' ')
    for i in range(len(wordList))[1:]:
        wordList[i] = '%20' + wordList[i]
    page = rq.get('https://tasty.co/search?q=' + ''.join(wordList))
    soup = BeautifulSoup(page.content, 'lxml')
    resultListing = []
    resultLinks = []
    for element in soup.find_all(class_='feed-item'):
        resultLinks.append(element['href'])
        for tag in element.find_all(class_='feed-item__title'):
            resultListing.append(tag.text)
    completeList = list(zip(resultListing, resultLinks))
    with open('results.txt', 'w') as file:
        for line in completeList:
            file.write(line[0] + "," + line[1] + "\n")
    # TODO: fix encoding of special characters
    print(completeList)
