from flask import Blueprint, render_template
#from app import create_app
todo = Blueprint('todo', __name__)
#todo = create_app()

from flask_login import (
        login_user,
        logout_user,
        current_user,
        login_required
        )

@todo.route('/')
def dashboard():
    return render_template('dashboard.html', current_user=current_user)

@todo.route('/notifications')
def notifications():
    print('here')
    return render_template('topNav/notifications.html', current_user=current_user)

@todo.route('/revenue')
def revenue():
    return render_template('revenue.html', current_user=current_user)

@todo.route('/analytics')
def analytics():
    return render_template('analytics.html', current_user=current_user)

#@todo.route('/notes')
#def notes():
#    return render_template('cards.html')

@todo.route('/wallets')
def wallets():
    return render_template('cards.html', current_user=current_user)

