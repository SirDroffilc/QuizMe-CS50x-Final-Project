from flask import render_template, Blueprint

from web_app.app import db

quiz = Blueprint('quiz', __name__, template_folder='templates')

@quiz.route('/')
def index():
    return render_template('quiz/index.html')

