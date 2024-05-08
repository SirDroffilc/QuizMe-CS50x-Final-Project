from flask import render_template, Blueprint

from web_app.app import db

profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/')
def index():
    return render_template('profile/index.html')

