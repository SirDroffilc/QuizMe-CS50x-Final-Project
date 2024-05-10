from flask import render_template, Blueprint, session, request, url_for, flash, redirect
from flask_login import current_user, login_required

from web_app.app import db
from web_app.models import User, Quiz, Item


quiz = Blueprint('quiz', __name__, template_folder='templates')

@quiz.route('/')
@login_required
def index():
    quizzes = current_user.quizzes
    return render_template('quiz/index.html', quizzes=quizzes)


@quiz.route('/create', methods=['GET', 'POST'])
@login_required
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
@login_required
def modify_quiz(quiz_id, quiz_title):
    quiz = Quiz.query.get(quiz_id)
    if current_user.id != quiz.user_id:
        return render_template('unauth.html')
    
    if request.method == 'GET':
        quiz_items = quiz.items
        return render_template('quiz/modify_quiz.html', quiz=quiz, quiz_items=quiz_items)
    
    elif request.method == 'POST':
        if 'new_title' in request.form.keys(): # change title
            newTitle = request.form.get('new_title')
            if newTitle:
                quiz.title = newTitle
                db.session.commit()
                flash(f'Title changed to {newTitle}', category="success")
            else:
                flash('Blank title is not allowed', category='error')

        elif 'new_instructions' in request.form.keys(): # update instructions
            new_instructions = request.form.get('new_instructions')
            if new_instructions:
                quiz.instructions = new_instructions
                db.session.commit()
                flash(f'Title changed to {new_instructions}', category="success")
            else:
                flash("Blank instruction is not allowed", category='error')
        
        elif 'question' in request.form.keys(): # add a question
            new_question = request.form.get('question')
            option1 = request.form.get('option1')
            option2 = request.form.get('option2')
            option3 = request.form.get('option3')
            option4 = request.form.get('option4')
            answer_key = request.form.get('answer_key')

            if not new_question or not option1 or not option2 or not option3 or not option4 or not answer_key:
                flash('Incomplete details', category='error')
                return redirect(url_for('quiz.modify_quiz', quiz_id=quiz.id, quiz_title=quiz.title))
            elif answer_key not in [option1, option2, option3, option4]:
                flash('Answer key must be in the options', category='error')
                return redirect(url_for('quiz.modify_quiz', quiz_id=quiz.id, quiz_title=quiz.title))
            
            new_item = Item(
                question=new_question,
                option1=option1, option2=option2, option3=option3, option4=option4, 
                answer_key=answer_key, quiz_id=quiz.id)
            db.session.add(new_item)
            quiz.total_items += 1
            db.session.commit()

            flash(f'Question added successfully', category='success')

        elif 'item_id' in request.form.keys(): # delete a question
            item_id = request.form.get('item_id')
            item_to_del = Item.query.get(item_id)
            db.session.delete(item_to_del)
            quiz.total_items -= 1
            db.session.commit()

        elif 'quiz_id' in request.form.keys(): # delete the quiz and redirect to index
            db.session.delete(quiz)
            db.session.commit()
            return redirect(url_for('quiz.index'))

        return redirect(url_for('quiz.modify_quiz', quiz_id=quiz.id, quiz_title=quiz.title))

@quiz.route('/all_quizzes')
@login_required
def all_quizzes():
    quizzes = Quiz.query.all()
    return render_template('quiz/all_quizzes.html', quizzes=quizzes)


@quiz.route('/answer_quiz/<int:quiz_id>/<string:quiz_title>', methods=['GET', 'POST'])
@login_required
def answer_quiz(quiz_id, quiz_title):
    quiz = Quiz.query.get(quiz_id)

    if request.method == 'GET':
        return render_template('quiz/answer_quiz.html', quiz=quiz)
    
    elif request.method == 'POST':
        score = 0
        selected_answers = {}
        for item in quiz.items:
            selected_answer = request.form.get('question{}'.format(quiz.items.index(item) + 1))
            selected_answers[item.id] = selected_answer
            if selected_answer == item.answer_key:
                score += 1
        return render_template('quiz/results.html', quiz=quiz, score=score, selected_answers=selected_answers)

        




    


