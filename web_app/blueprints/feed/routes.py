from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import current_user, login_required
from datetime import datetime, timezone

from web_app.app import db
from web_app.models import User, Post

feed = Blueprint('feed', __name__, template_folder='templates')

@feed.route('/')
@login_required
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('feed/index.html', posts=posts)


@feed.route('/post', methods=['POST'])
@login_required
def post():
    title = request.form.get('title')
    caption = request.form.get('caption')

    if not caption:
        flash('Post left blank.', category='error')
        return redirect(url_for('feed.index'))
    
    datetime_now = datetime.now(timezone.utc)
    
    new_post = Post(title=title, caption=caption, date=datetime_now, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('feed.index'))