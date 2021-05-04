from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .search import getResultsTasty
from .scraper import *
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    searchTermsDict = {}
    if request.method == 'POST':
        if "search" in request.form:
            search = request.form.get('search')
            if len(search) < 1:
                flash('Please enter search terms before submitting',
                      category='error')
            else:
                flash('Search Successful', category='success')
                searchTermsDict = getResultsTasty(search)
                titleList = list(searchTermsDict.keys())
                intoButtons = list(map(
                    lambda x: "<form method='POST' site_title='" + x + "'><button type='submit' class='btn btn-primary'>" + x + "</button><br /></form>", titleList))
                return render_template('home.html', user=current_user, siteButtons=intoButtons, siteTitlesDict=searchTermsDict)
        else:
            # siteToParse = 'tasty.co' + \
            #     searchTermsDict[request.form.get('id')]
            # print(siteToParse)
            # manipulate string so no apostrophes or parenthesis then join with -
            siteToParseTest = 'https://tasty.co/recipe/asian-chicken-chopped-salad'
            return redirect(url_for('views.viewRecipe', siteLink=siteToParseTest))
    return render_template('home.html', user=current_user)


@views.route('/view-recipe/<path:siteLink>', methods=['GET', 'POST'])
def viewRecipe(siteLink):

    title = getTitleTasty(siteLink)
    ingredientsList = getIngredientsTasty(siteLink)
    instructions = getInstructionsTasty(siteLink)

    return render_template("viewrecipe.html", siteTitle=title, ingredients=ingredientsList, instructions=instructions, user=current_user)
