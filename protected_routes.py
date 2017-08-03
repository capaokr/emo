from flask_app import app
from flask_login import login_required, current_user, logout_user
from flask import render_template, redirect, url_for, flash

@app.route('/logout')
def logout():
    if(current_user is None or not current_user.is_authenticated):
        flash('You need to be logged in in order to log out.')
    else:
        flash('You have been logged out.')
        logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', dashboard='active', sidedashboard='active')

@app.route('/train')
@login_required
def train():
    return render_template('dashboard.html', dashboard='active', train='active')

@app.route('/deploy')
@login_required
def deploy():
    return render_template('dashboard.html', dashboard='active', deploy='active')
