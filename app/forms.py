from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = TextField('Name', [validators.DataRequired()])
    email = TextField('Email', [validators.DataRequired()])
    subject = TextField('Subject', [validators.DataRequired()])
    message = TextAreaField('Message', [validators.DataRequired()])