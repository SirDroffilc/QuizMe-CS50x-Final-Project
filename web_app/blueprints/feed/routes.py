from flask import render_template, Blueprint

from web_app.app import db

feed = Blueprint('feed', __name__, template_folder='templates', static_folder='web_app/static')

@feed.route('/')
def index():
    return render_template('feed/index.html')

