from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .search import getResultsTasty
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    searchTermsDict = {}
    if request.method == 'POST':
        if "search-button" in request.form:
            search = request.form.get('search')
            if len(search) < 1:
                flash('Please enter search terms before submitting',
                      category='error')
            else:
                flash('Search Successful', category='success')
                searchTermsDict = getResultsTasty(search)
                titleList = list(searchTermsDict.keys())
                intoButtons = list(map(
                    lambda x: "<button class=\"list-group-item\" id=" + x + ">" + x + "</button>", titleList))
                print(intoButtons)
                return render_template('home.html', user=current_user, siteButtons=intoButtons, siteTitlesDict=searchTermsDict)
        else:
            siteToParse = 'tasty.co' + searchTermsDict[request.form.get('id')]
            print(siteToParse)
    return render_template('home.html', user=current_user)


@views.route('/view-recipe/')
