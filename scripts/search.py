import requests as rq
from bs4 import BeautifulSoup
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/search?terms=x')
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
            results[element['href']] = tag.text
    return jsonify(results)

    # with open('results.txt', 'w') as file:
    #     for line in completeList:
    #         file.write(line[0] + "," + line[1] + "\n")
    # TODO: fix encoding of special characters
