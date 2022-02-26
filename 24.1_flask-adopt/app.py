"""Pet Adoption Application"""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def show_list():
    """List all pets."""

    pets = Pet.query.all()
    return render_template("listing.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add pet form; handle adding."""

    form = AddPetForm()
    # species = db.session.query(Pet.species)
    # form.species.choices = species

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash((f"Added {name}"))
        return redirect('/')
    else:
        return render_template('/new.html', form=form)
