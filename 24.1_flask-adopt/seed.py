"""Seed file to make sample data for pets db."""

from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Make a bunch of users
p1 = Pet(name='Doug', species='dog', photo_url='https://images.pexels.com/photos/97082/weimaraner-puppy-dog-snout-97082.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', age=1, notes='Lovingly playful.', available=True)
p2 = Pet(name='Greta', species='dog', photo_url='https://images.pexels.com/photos/10660184/pexels-photo-10660184.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', age=9, notes='Gruff but tough', available=True)
p3 = Pet(name='Pizza', species='cat', photo_url='https://images.pexels.com/photos/156934/pexels-photo-156934.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', notes='Found her in an alley eating some pizza, super sweet', available=True)
p4 = Pet(name='Mr. Meaty', species='cat', photo_url='https://images.pexels.com/photos/991831/pexels-photo-991831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2', notes='Loves to eat mice, but probably should stop', available=True)
p5 = Pet(name='Franklin', species='turtle', notes='Adopted <3', available=False)

db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()