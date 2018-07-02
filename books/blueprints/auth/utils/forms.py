from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, HiddenField
from wtforms.validators import DataRequired, EqualTo, Length, Optional, Regexp
# from wtforms_components import EmailField, Email, Unique, PhoneNumberField


class PasswordResetForm(FlaskForm):
    reset_token = HiddenField()
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])

