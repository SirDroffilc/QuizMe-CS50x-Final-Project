from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from web_app.app import db
from web_app.models import Post, User

profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user = User.query.get(current_user.id)
    if request.method == 'GET':
        quizzes = current_user.quizzes
        total_items = 0
        for quiz in quizzes:
            total_items += len(quiz.items)
        posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.date.desc()).all()
        
        return render_template('profile/index.html', user=user, quizzes=quizzes, total_items=total_items, posts=posts)

    elif request.method == 'POST':
        

        if 'new_username' in request.form.keys():
            new_username = request.form.get('new_username')
            password = request.form.get('password')
            check_user = User.query.filter_by(username=new_username).first()

            if not new_username or not password:
                flash("Incomplete details.", category='error')
            elif not check_password_hash(user.password, password):
                flash("Incorrect Password. Please try again.", category='error')   
            elif check_user:
                flash('Username already taken.', category='error')     
            elif len(new_username) > 50 or len(new_username) < 3:
                flash('Username must be 3-50 characters.', category='error')
            else:
                user.username = new_username
                db.session.commit()
                flash(f"Username changed to {new_username}", category='success')
        
        elif 'new_password' in request.form.keys():
            old_password = request.form.get('old_password')
            new_password = request.form.get('new_password')
            new_password2 = request.form.get('new_password2')

            if not old_password or not new_password or not new_password2:
                flash("Incomplete details.", category='error')
            elif not check_password_hash(user.password, old_password):
                flash("Incorrect Old Password. Please try again.", category='error')  
            elif len(new_password) > 100 or len(new_password) < 8:
                flash('Password must be 8-100 characters.', category='error')
            elif new_password != new_password2:
                flash("Passwords don't match.", category='error')
            else:
                user.password = generate_password_hash(new_password)
                db.session.commit()
                flash("Password successfully changed", category='success')

        elif 'to_delete_id' in request.form.keys():
            password = request.form.get('password')
            if not password:
                flash('Incomplete details.', category='error')
            elif not check_password_hash(user.password, password):
                flash('Incorrect Password', category='error')
            else:
                flash(f'Account "{user.username}" successfully deleted')
                db.session.delete(user)
                db.session.commit()
                return redirect(url_for('auth.index'))
                
        return redirect(url_for('profile.index'))
        

