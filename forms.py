from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required
from application import *


class LoginForm(Form):
    name = StringField('Choose a display name', validators=[Required()])
    submit = SubmitField('Enter')

class CreateChannel(Form):
    room = StringField('Create new channel', validators=[Required()])
    submit = SubmitField('Enter')
