from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import LoginForm, RegistrationForm
from .utils import split_email
from ..api.app import db, bcrypt, login_manager
from .models import User

from flask_bcrypt import generate_password_hash

auth = Blueprint('auth', __name__)
#auth = create_app()

from flask_login import (
        login_user,
        logout_user,
        current_user,
        login_required,
        )

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        email_prefix = split_email(email)

        try:
            user = User.query.filter_by(email=email).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                flash(f'Login successful for {email_prefix}!', 'success')
                login_user(user)
                return redirect(url_for('todo.dashboard'))
            else:
                flash('Invalid email address or password', 'danger')
                print(f'Invalid username or password')
        except Exception as e:
            print(f"Error during log: {str(e)}")
            flash(e, 'danger')

    return render_template('auth/login.html',
                           title='Login',
                           form=form
                           )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if request.method=='POST':
            try:
                username = form.username.data
                email = form.email.data
                password = form.password.data

                newUser = User(
                        username=username,
                        email=email, 
                        password=bcrypt.generate_password_hash(password)
                        )
                db.session.add(newUser)
                db.session.commit()
                login_user(newUser)

                flash(f'Account created successfully for {form.username.data}!', 'success')
                return redirect(url_for('todo.dashboard'))
            except Exception as e:
                flash(f'Something went wrong during registration')
            except IntegrityError:
                db.session.rollback()
                flash(f"User already exists!.", "warning")
        #else:
            ##flash(f'Something went wrong during registration', 'danger')
    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('auth/forgot-password.html')

@login_required
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    print('logout successful')
    return redirect(url_for('auth.login'))

