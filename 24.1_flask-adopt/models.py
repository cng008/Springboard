"""Models for Pet Adoption Application."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_PET_IMG = 'https://media.istockphoto.com/vectors/continuous-line-dog-minimalistic-hand-drawing-vector-isolated-vector-id909324004?k=20&m=909324004&s=612x612&w=0&h=8NXfBg_oKfkJ1Rva6G_2PWYvK5RHP2BlSSOR6_7GvQ8='

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet -- bespoke or generic."""
        return self.photo_url or DEFAULT_PET_IMG
