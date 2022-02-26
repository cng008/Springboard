"""Seed file to make sample data for pets db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Make a bunch of users
p1 = Pet(name='Doug', species='dog', photo_url='https://i.pinimg.com/550x/7c/fd/33/7cfd33dd5692722650237a6411f28001.jpg', age=1, notes='Lovingly playful', available=True)
p2 = Pet(name='Greta', species='dog', photo_url='https://w0.peakpx.com/wallpaper/990/403/HD-wallpaper-walter-bull-dog-dogs-funny-meme-nelson-pitbull-terrier.jpg', age=9, notes='Gruff but tough', available=True)
p3 = Pet(name='Pizza', species='cat', photo_url='https://i.kym-cdn.com/entries/icons/facebook/000/027/852/Screen_Shot_2018-12-12_at_1.02.39_PM.jpg', notes='Found her in an alley eating some pizza, super sweet', available=True)
p4 = Pet(name='Mr. Meaty', species='cat', photo_url='https://i.pinimg.com/originals/59/54/b4/5954b408c66525ad932faa693a647e3f.jpg', notes='Loves to eat mice, but should probably stop', available=True)
p5 = Pet(name='Franklin', species='turtle', notes='Adopted <3', available=False)

db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()