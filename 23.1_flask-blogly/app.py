"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def show_list():
    """Redirect to list of users."""
    return redirect('/users')


@app.route('/users')
def list_users():
    """Show all users."""
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/users/new')
def create_user():
    """Show an add form for users"""
    return render_template('add_form.html')


@app.route('/users/new', methods=["POST"])
def add_user():
    """Process the add form, adding a new user and going back to /users"""
    first = request.form["first"]
    last = request.form["last"]
    image = request.form["image"]

    new_user = User(first_name=first, last_name=last, image_url=image)
    db.session.add(new_user)
    db.session.commit()

    flash("User has been created")

    return redirect(f'/users/{new_user.id}')


@app.route('/users/<int:user_id>')
def see_user(user_id):
    """Show information about the given user."""
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show the edit page for a user."""
    user = User.query.get_or_404(user_id)
    return render_template('edit_form.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def submit_edits(user_id):
    """Process the edit form, returning the user to the /users page."""
    first = request.form["first"]
    last = request.form["last"]
    image = request.form["image"]

    user = User.query.get_or_404(user_id)
    user.first_name = first
    user.last_name = last
    user.image_url = image

    db.session.add(user)
    db.session.commit()

    flash("User info has been saved")
    return redirect(f'/users')


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete the user."""
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    flash("User has been deleted")
    return redirect('/users')