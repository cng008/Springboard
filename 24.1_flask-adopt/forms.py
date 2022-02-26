from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dg','dog'), ('ct', 'cat'), ('tt', 'turtle')], validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available?', validators=[InputRequired()], default="checked")