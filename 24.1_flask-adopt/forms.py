from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Name')
    species = SelectField('Species')
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = StringField('Notes')
    available = BooleanField('Available?')