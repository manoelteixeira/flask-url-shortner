import click
from colorama import init, Fore
from sqlalchemy.exc import OperationalError

from app import db
from app.models import UrlModel

init(autoreset=True) # Coloroama

@click.command('init-db')
def init_db():
    '''
    Usage: $> Flask init-db 
    Drop all tables if any exists and create new tables.
    '''
    print(f'{Fore.GREEN}<<  Initializing Database.  >>') 
    
    try:
        print(f'{Fore.YELLOW}<<  Dropping all tables if exists  >>')
        db.drop_all()
       
        print(f'{Fore.YELLOW}<<  Creating Tables.  >>')
        db.create_all()
    except OperationalError as err:
        print(f'{Fore.RED}<<  Something Whent Wrong. Database not initialized.  >>')
        print(err)
        exit()
    else:
        print(f'{Fore.GREEN}<<  Verifying Database.  >>')
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        if len(tables) == 1 and 'url' in tables:
            print(f'{Fore.GREEN}<<  Done  >>')
        else:
            print(f'{Fore.RED}<<  Something Whent Wrong. Database not initialized.  >>')
    
    
