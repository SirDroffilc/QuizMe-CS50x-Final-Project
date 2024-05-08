from flask import render_template, Blueprint, session, request, url_for, flash, redirect
from flask_login import current_user, login_required

from web_app.app import db
from web_app.models import User, Quiz, Item


quiz = Blueprint('quiz', __name__, template_folder='templates')

@quiz.route('/')
def index():
    quizzes = current_user.quizzes
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
    if request.method == 'GET':
        quiz = Quiz.query.filter_by(id=quiz_id).first()
        return render_template('quiz/modify_quiz.html', quiz=quiz)
    elif request.method == 'POST':
        quiz = Quiz.query.filter_by(id=quiz_id).first()

        if 'new_title' in request.form.keys():
            newTitle = request.form.get('new_title')
            if newTitle:
                quiz.title = newTitle
                db.session.commit()
                flash(f'Title changed to {newTitle}', category="success")
            else:
                flash('Blank title is not allowed', category='error')

        elif 'new_instructions' in request.form.keys():
            new_instructions = request.form.get('new_instructions')
            if new_instructions:
                quiz.instructions = new_instructions
                db.session.commit()
                flash(f'Title changed to {new_instructions}', category="success")
            else:
                flash("Blank instructions is not allowed", category='error')
        
        elif 'question' in request.form.keys():
            new_question = request.form.get('question')
            answer_key = request.form.get('answer_key')

            pass

        return redirect(url_for('quiz.modify_quiz', quiz_id=quiz.id, quiz_title=quiz.title))


        




    


