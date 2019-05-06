from flask_wtf import FlaskForm, validators
from wtforms import DateTimeField, StringField, IntegerField, SubmitField, SelectField, validators

class AddEventForm(FlaskForm):
    description = StringField('Name of Event', validators=[validators.Length(min=4, max=25)])
    organizer = SelectField('Organizer', coerce=int)
    venue = StringField('Place of Event')
    start_time = DateTimeField('Starting from', format="%d-%m-%y")
    end_time = DateTimeField('Ending at', format="%d-%m-%y")
    submit = SubmitField('Add Event')