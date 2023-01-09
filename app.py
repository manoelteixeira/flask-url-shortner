from app import create_app


if __name__ == '__main__':
    # app = create_app(config_file='config.cfg')
    app = create_app()
    app.run(debug=False, host='0.0.0.0')
else:
    '''
    If app.py is runned using "flask run"
    '''
    # app = create_app(config_file='config.cfg')
    app = create_app()
    
