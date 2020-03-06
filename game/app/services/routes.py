from app import web_app
from flask import render_template

@web_app.route('/')
@web_app.route('/index')
def index():
    return render_template('index.html')

@web_app.route('/creategame')
def game():
    return render_template('creategame.html', id=str(1234556))