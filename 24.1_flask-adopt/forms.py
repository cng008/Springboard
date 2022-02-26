from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog','dog'), ('cat', 'cat'), ('turtle', 'turtle')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()], default="checked")


class EditPetForm(FlaskForm):
    """Form for adding pets."""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()], default="checked")