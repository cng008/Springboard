from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog','Dog'), ('cat', 'Cat'), ('turtle', 'Turtle')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()], default="checked")


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()], default="checked")