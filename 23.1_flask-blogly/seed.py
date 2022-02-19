"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
pete = User(first_name='Pete', last_name='Davidson', image_url='https://static01.nyt.com/images/2018/12/16/world/16xp-davidson1/merlin_146914890_3e2b450f-94bf-472f-b717-a7b8b4004b1a-superJumbo.jpg')
kanye = User(first_name='Kanye', last_name='West', image_url='https://cdn.justjared.com/wp-content/uploads/headlines/2022/02/kanye-west-announces-donda-2-will-only-be-on-stem-player.jpg')
kim = User(first_name='Kim', last_name='Kardashian', image_url='https://media1.popsugar-assets.com/files/thumbor/mzUiLo-8Y10peZM55u_w6Loa-h4/612x451:2344x2183/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2019/11/19/007/n/1922398/d3c823415dd4769f7d9263.82518194_/i/Kim-Kardashian.jpg')

# Add new objects to session, so they'll persist
db.session.add(pete)
db.session.add(kanye)
db.session.add(kim)

# Commit--otherwise, this never gets saved!
db.session.commit()
