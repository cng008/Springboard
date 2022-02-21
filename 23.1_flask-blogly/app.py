"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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


@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""
    return render_template('404.html'), 404
    
########### USERS ###################################################

@app.route('/users')
def list_users():
    """Show all users."""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('/users/list.html', users=users)


@app.route('/users/new')
def create_user():
    """Show an add form for users"""
    return render_template('/users/new.html')


@app.route('/users/new', methods=["POST"])
def add_user():
    """Process the add form, adding a new user and going back to /users"""

    new_user = User(
        first_name = request.form["first"], 
        last_name = request.form["last"], 
        image_url = request.form["image"] or None)

    db.session.add(new_user)
    db.session.commit()

    flash(f"User '{new_user.full_name}' has been added")
    return redirect(f'/users/{new_user.id}')


@app.route('/users/<int:user_id>')
def see_user(user_id):
    """Show information about the given user."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id)
    return render_template('/users/details.html', user=user, posts=posts)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """Show the edit page for a user."""
    user = User.query.get_or_404(user_id)
    return render_template('/users/edit.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def submit_edits(user_id):
    """Process the edit form, returning the user to the /users page."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first"]
    user.last_name = request.form["last"]
    user.image_url = request.form["image"]

    db.session.add(user)
    db.session.commit()

    flash("User info has been saved")
    return redirect(f'/users')


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete the user."""
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    flash(f"User '{user.full_name}' has been deleted")
    return redirect('/users')


########### POSTS ###################################################

@app.route('/users/<int:user_id>/posts/new')
def create_post(user_id):
    """Show form to add a post for that user."""
    user = User.query.get_or_404(user_id)
    return render_template('/posts/new.html', user=user)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Handle add form; add post and redirect to the user detail page."""
    user = User.query.get_or_404(user_id)
    new_post = Post(
        title = request.form["title"], 
        content = request.form["content"],
        user_id = user_id)

    db.session.add(new_post)
    db.session.commit()

    flash(f"'{new_post.title}' has been added.")
    return redirect(f'/users/{user.id}')


@app.route('/posts/<int:post_id>')
def see_post(post_id):
    """Show a post. Show buttons to edit and delete the post."""
    post = Post.query.get_or_404(post_id)
    return render_template('/posts/show.html', post=post)


@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show form to edit a post, and to cancel (back to user page)."""
    post = Post.query.get_or_404(post_id)
    return render_template('/posts/edit.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def submit_post(post_id):
    """Handle editing of a post. Redirect back to the post view."""
    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    flash(f"Post '{post.title}' has been updated.")
    return redirect(f'/posts/{post_id}')


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete the post."""
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    flash(f"Post '{post.title}' has been deleted.")
    return redirect(f"/users/{post.user_id}")
