from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    app.secret_key = 'njcidjw2l1;a2@fnid&82(8@)'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @login_manager.unauthorized_handler
    def unauthorized():
        return render_template('unauth.html')

    # imports
    from web_app.blueprints.auth.routes import auth
    from web_app.blueprints.feed.routes import feed
    from web_app.blueprints.quiz.routes import quiz
    from web_app.blueprints.profile.routes import profile

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(feed, url_prefix='/feed')
    app.register_blueprint(quiz, url_prefix='/quiz')
    app.register_blueprint(profile, url_prefix='/profile')

    migrate = Migrate(app, db)

    return app