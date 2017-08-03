from flask_app import app, serializer
from flask import render_template, redirect, url_for, flash
from forms import LoginForm
from flask_login import current_user

@app.route('/')
def index():
    return render_template('index.html', home='active')

@app.route('/about')
def about():
    return render_template('about.html', about='active')

@app.route('/howto')
def howto():
    return render_template('howto.html', howto='active')

@app.route('/login', methods=['GET'])
def login():
    if(current_user.is_authenticated):
        flash('You are already logged in.')
        return redirect(url_for('index'))
    form = LoginForm()
    return render_template('login.html', login='active', form = form)

@app.route('/test')
def test():
    return serializer.dumps([app.config['ADMIN_ACCOUNT'], app.config['ADMIN_KEY']])
