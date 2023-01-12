from flask import Blueprint, flash, render_template, url_for, redirect

from app import db
from app.models import UrlModel
from app.forms import UrlForm

bp = Blueprint(name='index',
               import_name=__name__,
               url_prefix='/')

@bp.route(rule='/', methods=['GET', 'POST'])
def index():
    '''
    Home page
    '''
    form = UrlForm()
    
    return render_template('index.html',
                           form=form)
    
@bp.route(rule='/<string:key>', methods=['GET'])
def redirect_key(key:str):
    url = UrlModel.query.filter_by(key=key).first()
    if not url:
        flash(message='URL Not Found',
              category='info')
        return redirect(url_for('index.index'))
    return redirect(location=url.url)

