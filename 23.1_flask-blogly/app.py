"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

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
    """Show recent list of posts, most-recent first."""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("posts/homepage.html", posts=posts)


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


@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        new_user = User(
        first_name = request.form["first"], 
        last_name = request.form["last"], 
        image_url = request.form["image"] or None)

        db.session.add(new_user)
        db.session.commit()

        flash(f"User '{new_user.full_name}' added")
        return redirect(f'/users/{new_user.id}')

    else:
        """Show an add form for users"""
        return render_template('/users/new.html')


@app.route('/users/<int:user_id>')
def see_user(user_id):
    """Show information about the given user."""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id)
    return render_template('/users/details.html', user=user, posts=posts)


@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        """Process the edit form, returning the user to the /users page."""
        user = User.query.get_or_404(user_id)
        user.first_name = request.form["first"]
        user.last_name = request.form["last"]
        user.image_url = request.form["image"]

        db.session.add(user)
        db.session.commit()

        flash("User info saved")
        return redirect('/users')

    else:
        """Show the edit page for a user."""
        user = User.query.get_or_404(user_id)
        return render_template('/users/edit.html', user=user)


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete the user."""
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    flash(f"User '{user.full_name}' deleted")
    return redirect('/users')


########### POSTS ###################################################

@app.route('/users/<int:user_id>/posts/new', methods=['GET', 'POST'])
def create_post(user_id):
    if request.method == 'POST':
        """Handle add form; add post and redirect to the user detail page."""
        user = User.query.get_or_404(user_id)
        
        tag_ids = [int(num) for num in request.form.getlist("tags")]
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

        new_post = Post(
            title = request.form["title"], 
            content = request.form["content"],
            user = user,
            tag=tags)

        db.session.add(new_post)
        db.session.commit()

        flash(f"'{new_post.title}' has been added.")
        return redirect(f'/users/{user.id}')

    else:
        """Show form to add a post for that user."""
        user = User.query.get_or_404(user_id)
        tags = Tag.query.all()
        return render_template('/posts/new.html', user=user, tags=tags)


@app.route('/posts/<int:post_id>')
def see_post(post_id):
    """Show a post. Show buttons to edit and delete the post."""
    post = Post.query.get_or_404(post_id)
    return render_template('/posts/show.html', post=post)


@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    if request.method == 'POST':
        """Handle editing of a post. Redirect back to the post view."""
        post = Post.query.get_or_404(post_id)
        post.title = request.form["title"]
        post.content = request.form["content"]

        tag_ids = [int(num) for num in request.form.getlist("tags")]
        post.tag = Tag.query.filter(Tag.id.in_(tag_ids)).all()

        db.session.add(post)
        db.session.commit()

        flash(f"Post '{post.title}' has been updated.")
        return redirect(f'/posts/{post_id}')

    else:
        """Show form to edit a post, and to cancel (back to user page)."""
        post = Post.query.get_or_404(post_id)
        tags = Tag.query.all()
        return render_template('/posts/edit.html', post=post, tags=tags)


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete the post."""
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    flash(f"Post '{post.title}' has been deleted.")
    return redirect(f"/users/{post.user_id}")


########### TAGS ###################################################

@app.route('/tags')
def list_tags():
    """Lists all tags, with links to the tag detail page."""
    tags = Tag.query.all()
    return render_template('/tags/list.html', tags=tags)


@app.route('/tags/new', methods=['GET', 'POST'])
def create_tag():
    if request.method == 'POST':
        """Process add form, adds tag, and redirect to tag list."""
        post_id = [int(num) for num in request.form.getlist("posts")]
        posts = Post.query.filter(Post.id.in_(post_id)).all()
        new_tag = Tag(name=request.form["tag"], post=posts)

        db.session.add(new_tag)
        db.session.commit()

        flash(f"'{new_tag.name}' tag added.")
        return redirect('/tags')

    else:
        """Shows a form to add a new tag."""
        posts = Post.query.all()
        return render_template('tags/new.html', posts=posts)


@app.route('/tags/<int:tag_id>')
def see_tag(tag_id):
    """Show detail about a tag. Have links to edit form and to delete."""
    tag = Tag.query.get_or_404(tag_id)
    return render_template('/tags/show.html', tag=tag)


@app.route('/tags/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    if request.method == 'POST':
        """Process edit form, edit tag, and redirects to the tags list."""
        tag = Tag.query.get_or_404(tag_id)
        tag.name = request.form["tag"]
        post_ids = [int(num) for num in request.form.getlist("posts")]
        tag.post = Post.query.filter(Post.id.in_(post_ids)).all()

        db.session.add(tag)
        db.session.commit()

        flash(f"'{tag.name}' tag edited.")
        return redirect('/tags')

    else:
        """Show edit form for a tag."""
        tag = Tag.query.get_or_404(tag_id)
        posts = Post.query.all()
        return render_template('/tags/edit.html', tag=tag, posts=posts)


@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    """Delete a tag."""
    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    flash(f"Tag '{tag.name}' deleted.")
    return redirect("/tags")
