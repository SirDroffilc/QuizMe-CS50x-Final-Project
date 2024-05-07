from flask import render_template, Blueprint

from web_app.app import db

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/')
def index():
    return render_template('auth/index.html')

