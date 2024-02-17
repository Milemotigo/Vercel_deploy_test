import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    '''
    basedir makes it easier to organize
    and locate files like databases
    consistently throughout your program
    '''
    app.config['SECRET_KEY'] = '7c46044f81919a429e07cdb5a76dcee4'
    @app.route('/', methods=['GET'])
    def home():
        return render_template('home.html')
    return app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True, port='8000')
