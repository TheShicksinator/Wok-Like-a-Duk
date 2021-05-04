from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
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
            # siteAddition = searchTermsDict[request.form.get('id')]
            # siteAddition.strip()
            # siteAddition = siteAddition.replace('(', '')
            # siteAddition = siteAddition.replace(')', '')
            # siteAddition = siteAddition.replace(',', '')
            # siteAddition = siteAddition.replace("'", '')
            # siteAddition = siteAddition.replace(' ', '-')
            # siteToParse = 'tasty.co' + siteAddition
            # manipulate string so no apostrophes or parenthesis then join with -

            # WORKAROUND. request.form.get('id') returns None for reasons I cannot explain,
            # if it correctly returned a string the commented out code above would work:
            siteToParse = 'https://tasty.co/recipe/asian-chicken-chopped-salad'
            return redirect(url_for('views.viewRecipe', siteLink=siteToParse))
    return render_template('home.html', user=current_user)


@views.route('/view-recipe/<path:siteLink>', methods=['GET', 'POST'])
def viewRecipe(siteLink):

    title = getTitleTasty(siteLink)
    ingredientsList = getIngredientsTasty(siteLink)
    instructions = getInstructionsTasty(siteLink)
    file = open('shopping-list.txt', 'w', encoding='utf-8')
    for number, ingredient in enumerate(ingredientsList):
        file.write(f"{number}: {ingredient}\n")
    file.close()

    return render_template("viewrecipe.html", siteTitle=title, ingredients=ingredientsList, instructions=instructions, user=current_user)


@views.route('/download')
def download():
    path = "shopping-list.txt"
    return send_file(path, as_attachment=True)
