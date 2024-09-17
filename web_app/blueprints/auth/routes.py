from flask import render_template, Blueprint, request, url_for, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from web_app.app import db
from web_app.models import User

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/')
def index():
    return render_template('auth/index.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')
    
    elif request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2= request.form.get('password2')

        if not username or not password1:
            flash('Incomplete Details.', category='error')
            return redirect(url_for('auth.signup'))
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already taken.', category='error')
            return redirect(url_for('auth.signup'))
        elif len(username) > 50 or len(username) < 3:
            flash('Username must be 3-50 characters.', category='error')
            return redirect(url_for('auth.signup'))
        elif len(password1) > 100 or len(password1) < 8:
            flash('Password must be 8-100 characters.', category='error')
            return redirect(url_for('auth.signup'))
        elif password1 != password2:
            flash("Passwords don't match", category='error')
            return redirect(url_for('auth.signup'))
        else:
            hashed_pw = generate_password_hash(password1)
            new_user = User(username=username, password=hashed_pw)

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account successfully created!", category='success')
            return redirect(url_for('feed.index'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Incomplete Details.', category='error')
            return redirect(url_for('auth.signup'))
        
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('feed.index'))
            else:
                flash('Incorrect password', category='error')
                return redirect(url_for('auth.login'))
        else:
            flash('Username not found', category='error')       
            return redirect(url_for('auth.index')) 


@auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('Logged Out.', category='success')
    return redirect(url_for('auth.index'))