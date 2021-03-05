from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('Password')

        user = User.query.filter_by(email=email).first()

        if user:

            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            else:
                flash('Error - Incorrect Password', category='error')

        else:
            flash('Error - Email doesn\'t exists', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/logout')
@login_required
def logout():
    flash(f'{current_user.first_name} Logged out', category='error')
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('email')
        Fname = request.form.get('Firstname')
        password = request.form.get('Password')
        PassCheck = request.form.get('PasswordCheck')
        
        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already in use", category='error')

        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
            

        elif len(Fname) < 2:
            flash("First name must be greater than 2 characters", category="error")

        elif password != PassCheck:
            flash("Passwords Don't Match", category="error")

        elif len(password) < 7:
            flash("Password must be greater than 7 characters", category="error")

        else:
            new_user = User(email=email, first_name=Fname, password=generate_password_hash(password, method='sha256'))
            user = new_user
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category="success")
            login_user(user, remember=True)
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)
