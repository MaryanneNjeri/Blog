from  flask_wtf import FlaskForm
from wtfforms import StringField,PasswordField,SubmitField
from  wtfforms.validators import Required,Email,EqualTo
from ..models import Writer
from wtfforms import ValidationError
'''
we import the validators that help us ensure proper email structure is followed
'''
class Registration(FlaskForm):
    username=StringField('Enter your username',validators=[Required()])
    email=StringField('Enter your email',validators=[Required()])
    password=PasswordField('password',validators=[Required(),
    EqualTo('password_confirm',message ='Password must match')])
    password_confirm= PasswordField('confirm passwords',validators=[Required()])
    submit = SubmitField('Sign Up')
class Registration(FlaskForm):
    def validate_email(self,data_field):
        if Writer.query.filter_by(email=data_field.data).first():
            raise ValidationError('Sorry there is an account with that email')
    def validate_username(self,data_field):
        if Writer.query.filter_by(username = data_field.data).first():
            raise ValidationError('Sorry that user name is taken')
