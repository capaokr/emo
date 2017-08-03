from flask_app import app, serializer
from flask import request, redirect, url_for, flash
from models import Users
from flask_login import login_user

@app.route('/login', methods=['POST'])
def verify():
    username = request.form['username']
    password = request.form['password']
    user = Users(username, password)
    if(username == app.config['ADMIN_ACCOUNT'] and password == app.config['ADMIN_KEY']):
        login_user(user)
        flash('You have successfully logged in.')
        returnpage = 'dashboard'
    else:
        flash('Invalid credentials.')
        returnpage = 'login'
    return redirect(url_for(returnpage))
