from flask import Blueprint, render_template, flash, redirect, url_for


events_blueprint = Blueprint('events',
    __name__,
    template_folder='../../templates/events')

from src.components.events.forms import AddEventForm
from src.models.user import User
from src.models.event import Event
from src import db

@events_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    # print("Hello")
    form = AddEventForm()    
    # print(form)
    form.organizer.choices = [(u.id, u.email) for u in User.query.all()]  
    if form.validate_on_submit():
        e = Event(description=form.description.data, user_id=form.organizer.data)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('ticket'))
    return render_template('add_event.html', form=form)

@events_blueprint.route('/list')
def list():
    return "here are all the events"

