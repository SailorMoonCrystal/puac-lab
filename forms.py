from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField


class ContactForm(FlaskForm):
    name = TextField("Nick")
    email = TextField("Email")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
