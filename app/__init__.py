import click
from os import makedirs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # Ensure the instance folder exists
    try:
        makedirs(app.instance_path)
        print('<< instance folder created. >>')
    except OSError:
        print('<< instance folder found. >>')
    
    # Setup flask instance
    if config_file:
        app.config.from_file(config_file)
        print('<< Configuration file loaded. >>')
    else:
        print('<< Configuration file not found. Using default configuration >>')
        app.config['SECRET_KEY'] = 'you-will-never-guess'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortner_data.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Intialize extensions
    initialize_extensions(app=app)
    
    # Register Blueprints
    register_blueprint(app=app)    
    
    # Hello World =D    
    # @app.route('/hello')
    # def hello():
    #     return "<h1>Hello World!</h1>"
    
    return app
    

def register_blueprint(app):
    '''
    Register blueprints (Routes) 
    '''
    from app.url_shortner import bp
    app.register_blueprint(bp)


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    
    # SQLAlchemy configuration
    db.init_app(app)
    with app.app_context():
        app.cli.add_command(init_db)
        
    
@click.command('init-db')
def init_db():
    '''
    Usage: $> Flask init-db 
    Drop all tables if any exists and create new tables.
    '''
    
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    if len(tables) > 0:
        print('\n-=-=-=-=-\nDropping all existing tables.')
        db.drop_all()
    print('-=-=-=-=-\nCreating tables.\n-=-=-=-=-\n')
    db.create_all()