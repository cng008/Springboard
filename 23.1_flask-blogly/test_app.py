from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don"t clutter tests with SQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_ECHO"] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config["TESTING"] = True

# This is a bit of hack, but don"t use Flask DebugToolbar
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

db.drop_all()
db.create_all()


class UserTests(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample User."""

        User.query.delete()

        new_user = User(first_name="Virgil", last_name="Ablo", image_url="https://images.wsj.net/im-442226?width=860&size=1.5&pixel_ratio=1.5")
        db.session.add(new_user)
        db.session.commit()

        self.user_id = new_user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Virgil", html)

    def test_see_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Virgil Ablo</h1>", html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first": "Ye", "last": "West", "image": "https://media1.popsugar-assets.com/files/thumbor/mzUiLo-8Y10peZM55u_w6Loa-h4/612x451:2344x2183/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2019/11/19/007/n/1922398/d3c823415dd4769f7d9263.82518194_/i/Kim-Kardashian.jpg"}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Ye West</h1>", html)

    def test_edit_user(self):
        with app.test_client() as client:
            d = {"first": "Virgil", "last": "Abloh", "image": "https://images.wsj.net/im-442226?width=860&size=1.5&pixel_ratio=1.5"}
            resp = client.post(f"/users/{self.user_id}/edit", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)


class PostTests(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample User."""

        Post.query.delete()

        user = User(first_name="Virgil", last_name="Abloh", image_url="https://images.wsj.net/im-442226?width=860&size=1.5&pixel_ratio=1.5")
        db.session.add(user)
        db.session.commit()

        post = Post(title='Free Game', content='https://virgilabloh.org/free-game/', created_at='2022-02-16 17:43:07.625859', user_id=1)
        db.session.add(post)
        db.session.commit()

        self.post_id = post.id
        self.post = post
        self.post.user.id = post.user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()


    def test_see_post(self):
        with app.test_client() as client:
            resp = client.get(f"/posts/{self.post_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Free Game</h1>", html)


    def test_add_post(self):
        with app.test_client() as client:
            d = {"title": "Off-White Drop @ 10pm ET today", "content": "Collaboration with LV"}
            resp = client.post(f"/users/1/posts/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Off-White Drop @ 10pm ET today", html)
            
    def test_edit_post(self):
        with app.test_client() as client:
            d = {"title": "Free Game", "content": "CORRECTION: https://virgilabloh.com/free-game"}
            resp = client.post(f"/users/1/posts/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Free Game", html)