from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
   sender = EmailField('sender',
                       validators=[DataRequired()])
   subject = StringField('subject',
                         validators=[DataRequired()]) 
   content = TextAreaField('content',
                           validators=[DataRequired()]) 
