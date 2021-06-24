from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, DateTimeField


class UserForm(FlaskForm):
    name=TextField("Nick")
    message = TextAreaField("Message")
    submit = SubmitField("Send")

class ContactForm(UserForm):
    email = TextField("Email")


class GuestBookForm(UserForm):
    date = DateTimeField("Date")
   

