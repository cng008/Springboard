"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    image_url = db.Column(db.String, nullable=False, default=DEFAULT_IMG_URL)
   
    # Sets up a user attribute on each instance of Post.
    # SQLA will populate it with data from the users table automatically
    # When a user is deleted, the related posts should be deleted, too.
    posts = db.relationship('Post', backref='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>"
    
    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.String(400),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Post id={self.id} title={self.title} content={self.content} created_at={self.created_at} user={self.user.id}>"

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""
        return self.created_at.strftime("%b %-d,  %Y @ %-I:%M %p")

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False)

    post = db.relationship('Post', secondary='post_tags', cascade="all,delete", backref='tag')
    
    def __repr__(self):
        return f"<Tag id={self.id} name={self.name}>"

class PostTag(db.Model):
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    # buffer = db.Column(db.Text)
    