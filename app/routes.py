from app import app
from flask import request, redirect, url_for, render_template

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/search/', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form['query'])
        return request.form['query']
    else:
        return redirect(url_for('home'))