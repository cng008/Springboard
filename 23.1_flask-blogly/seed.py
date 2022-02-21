"""Seed file to make sample data for users db."""

from models import db, User, Post
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Make a bunch of users
pete = User(first_name='Pete', last_name='Davidson', image_url='https://static01.nyt.com/images/2018/12/16/world/16xp-davidson1/merlin_146914890_3e2b450f-94bf-472f-b717-a7b8b4004b1a-superJumbo.jpg')
kanye = User(first_name='Kanye', last_name='West', image_url='https://cdn.justjared.com/wp-content/uploads/headlines/2022/02/kanye-west-announces-donda-2-will-only-be-on-stem-player.jpg')
kim = User(first_name='Kim', last_name='Kardashian', image_url='https://media1.popsugar-assets.com/files/thumbor/mzUiLo-8Y10peZM55u_w6Loa-h4/612x451:2344x2183/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2019/11/19/007/n/1922398/d3c823415dd4769f7d9263.82518194_/i/Kim-Kardashian.jpg')

db.session.add_all([pete, kanye, kim])

# Commit first so posts table can reference users
db.session.commit()

# Make a bunch of posts
kan1 = Post(title='Donda 2', content='Only available on stem player', created_at='2022-02-16 17:43:07.625859', user_id='2')
kan2 = Post(title='Jeen-Yuhs', content='Episode 1 on Netflix now', created_at='2022-02-14 12:43:07.625859', user_id='2')
kan3 = Post(title='Thoughts', content='I post what I want', created_at='2022-02-13 09:13:07.625859', user_id='2')

kim1 = Post(title='House Tour', content='Love my backyard', created_at='2022-02-16 17:39:07.625859', user_id='3')
kim2 = Post(title='Tik Tok', content='It is fun', created_at='2022-02-13 12:39:07.625859', user_id='3')
kim3 = Post(title='Kids', content='Love my kids', created_at='2022-02-14 09:08:07.625859', user_id='3')

pet1 = Post(title='Back to work', content='Going live tonight on SNL', created_at='2022-02-16 20:39:07.625859', user_id='1')
pet2 = Post(title='Jokes', content='Knock knock', created_at='2022-02-20 21:23:07.625859', user_id='1')
pet3 = Post(title='BRB', content='Taking a break from social media', created_at='2022-02-20 23:43:07.625859', user_id='1')

db.session.add_all([kan1, kan2, kan3, kim1, kim2, kim3, pet1, pet2, pet3])

db.session.commit()
