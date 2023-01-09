from flask import Blueprint, flash, render_template, url_for, redirect

from app import db

bp = Blueprint(name='index',
               import_name=__name__,
               url_prefix='/')

@bp.route(rule='/', methods=['GET', 'POST'])
def index():
    '''
    Home page
    '''
    return "<h1>Hello World</h1>"