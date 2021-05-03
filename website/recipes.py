from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User
from .search import getResultsTasty
recipes = Blueprint('recipes', __name__)


@recipes.route('/search-results', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        search = request.form.get('search')
        return render_template('search_results.html', search=getResultsTasty(search))


@recipes.route('/saved-recipes', methods=['GET', 'POST'])
@login_required
def saved_recipes():
    if request.method == 'POST':
        recipes = current_user.recipes


@recipes.route('/view-recipes', methods=['GET', 'POST'])
def view_recipes():
    pass
