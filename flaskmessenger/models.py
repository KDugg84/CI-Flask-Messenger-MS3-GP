from flaskmessenger import db, login_manager
from datetime import datetime
from flask_login import UserMixin


# function with a decorator used for reloading the user from the user id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # schema for the User model
    # unique id for each user based on a primary key
    id = db.Column(db.Integer, primary_key=True)

    # we want user accounts to be unique
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # allows users to register with a default profile picture
    profile_image = db.Column(db.String(23), nullable=False,
                           default='profile.png')
    password = db.Column(db.String(60), nullable=False)

    # post attribute has a relationship with the Post Model
    # backref 'author' attribute allows to get the user who created the post
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"User('{self.username}', '{self.email}', '{self.profile_image}')"


class Post(db.Model):
    # schema for the Post model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Post('{self.title}', '{self.date_posted}')"        