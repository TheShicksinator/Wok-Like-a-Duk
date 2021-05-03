from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .search import getResultsTasty
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        search = request.form.get('search')
        if len(search) < 1:
            flash('Please enter search terms before submitting', category='error')
        else:
            flash('Search Successful', category='success')
            searchTermsDict = getResultsTasty(search)
            titleList = list(searchTermsDict.keys())
            return render_template('home.html', user=current_user, siteTitles=titleList)
    return render_template('home.html', user=current_user)
