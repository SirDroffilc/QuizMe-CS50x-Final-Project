from flask import render_template, Blueprint, session, request, url_for, flash, redirect
from flask_login import current_user, login_required

from web_app.app import db
from web_app.models import User, Quiz, Item


quiz = Blueprint('quiz', __name__, template_folder='templates')

@quiz.route('/')
def index():
    quizzes = Quiz.query.filter_by(user_id=current_user.id)
    return render_template('quiz/index.html', quizzes=quizzes)


@quiz.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('quiz/create.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        instructions = request.form.get('instructions')

        if not title:
            title = f'Untitled Quiz by {current_user.username}'
        elif len(title) > 30:
            flash('Title must be at most 30 characters', category='error')
            return redirect(url_for('quiz.create'))

        if not instructions:
            instructions = "Answer the following items"

        new_quiz = Quiz(title=title, instructions=instructions, total_items=0, user_id=current_user.id)
        db.session.add(new_quiz)
        db.session.commit()

        flash(f"Quiz '{title}' successfully created!", category='success')
        return redirect(url_for('quiz.index'))
    

@quiz.route('/modify_quiz/<int:quiz_id>/<string:quiz_title>', methods=['GET', 'POST'])
def modify_quiz(quiz_id, quiz_title):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    return render_template('quiz/modify_quiz.html', quiz=quiz)




    


