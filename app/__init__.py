# import click
from os import makedirs, environ, path
from colorama import init ,Fore 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


init(autoreset=True) # Colorama setup

db = SQLAlchemy()


def create_app(config_file:str=None):
    app = Flask(__name__)
    app.config['BASE_DIR'] = path.abspath(path.curdir)
    # Make Sure instance folder exist
    if not path.isdir(app.instance_path):
        print(f'{Fore.RED}<<  Intance folder not found - Setting up instance  >> ')
        try:
            makedirs(app.instance_path)
        except OSError:
            print(f'{Fore.RED}instance folder could not be created.')
            exit()
    else:
        print(f'{Fore.GREEN}<<  Intance folder found.  >>')
        
    # Flask App configuration setup
    if config_file and path.isfile(path.join(app.config['BASE_DIR'], config_file)):
        app.config['APPLICATION_SETTINGS'] = path.join(app.config['BASE_DIR'], config_file)
    else:
        app.config['APPLICATION_SETTINGS'] = path.join(app.config['BASE_DIR'], environ.get('APPLICATION_SETTINGS'))
    
    # Load configurations
    if path.isfile(app.config['APPLICATION_SETTINGS']):
        app.config.from_pyfile(app.config['APPLICATION_SETTINGS'])
        print(f'{Fore.GREEN}<<  Configuration file loaded.  >>')
    else:
        print(f'{Fore.RED}<<  Configuration file not found.  >>')
        print(f'{Fore.YELLOW}<<  Loading default configuration.  >>\n{Fore.RED}<<  DEFAULT CONFIGURATION IS NOT SAFE.  >>')
        app.config['SECRET_KEY'] = 'you-will-never-guess'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.sqlite'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    if path.isfile(path.join(app.config['BASE_DIR'], 'instance/app_data.sqlite')):
        print(f'{Fore.GREEN}<<  Database found.  >>')
    else:
        print(f'{Fore.RED}<<  Database not found.  >>')
        print(f'<<  Use "flask init-db" to initialize database  >>')
    
    # Intialize extensions
    initialize_extensions(app=app)
    
    # Register Blueprints
    register_blueprint(app=app)    
    
    return app
    

def register_blueprint(app):
    '''
    Register blueprints (Routes) 
    '''
    from app.blueprints import shortner_bp, index_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(shortner_bp)


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    
    # SQLAlchemy configuration
    db.init_app(app)
    from app.utils.commands import init_db
    with app.app_context():
        app.cli.add_command(init_db)
        
