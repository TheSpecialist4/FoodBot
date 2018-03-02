from app import app
from flask import request, redirect, url_for

@app.route('/')
@app.route('/home/')
def home():
    return '<form action = "http://localhost:5000/search/" method = "POST"><input type = "text" name = "query" placeholder = "Search.."/><input type = "submit" value = "submit"/></form>'

@app.route('/search/', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form['query'])
        return request.form['query']
    else:
        return redirect(url_for('home'))