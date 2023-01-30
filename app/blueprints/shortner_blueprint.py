from flask import Blueprint, flash, url_for, redirect
from sqlalchemy.exc import IntegrityError
from app import db
from app.forms import UrlForm
from app.models import UrlModel
from app.utils import get_key


bp = Blueprint(name='shortner',
               import_name=__name__,
               url_prefix='/')

@bp.route(rule='/shortner', methods=['POST'])
def add_url():
    '''
    Short URL
    '''
    form = UrlForm()
    if form.validate_on_submit():
        original_url = form.url.data
        url = UrlModel.query.filter_by(url=original_url).first()
        if url:
            flash(message=url.key,
                  category='short-url')
            return redirect(url_for('index.index'))
        key = get_key(size=7)
        new_url = UrlModel(original_url, key)
        try:
            db.session.add(new_url)
            db.session.commit()
        except IntegrityError as err:
            db.session.rollback()
        
        flash(message=key,
              category='short-url')
    
    return redirect(url_for('index.index'))