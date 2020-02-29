from app import app
from flask import render_template

@app.route('/')
def index():
    name='Evgeny'
    return render_template('index.html',name=name)

@app.errorhandler(404)
def Page_not_found(e):
    return render_template('404.html'),404