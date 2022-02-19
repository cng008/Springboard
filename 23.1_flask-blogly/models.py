"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = 'https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png'


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    image_url = db.Column(db.String, nullable=False, default='https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png')

    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>"
    
    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"
