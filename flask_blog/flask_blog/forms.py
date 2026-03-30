# Forms and User Input are so common, we don't have to reinvent the wheel. WT-Forms is available for use
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed # Allow uploading files. FileAllowed is a validator to choose which files are allowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User
from flask_login import current_user
# We write Python classes that are representative of our forms, and they will be automatically converted to HTML forms within our template

class RegistrationForm(FlaskForm):
    username = StringField("Username Here", validators=[DataRequired(), Length(min=2, max=20)]) # Username is also label in our HTML
    
    email = StringField("Email", validators=[DataRequired(), Email()])
    
    password = PasswordField("Password Here", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    
    submit = SubmitField("Sign Up")
    
    # validation template
    # def validate_field(self, field):
    #     if True:
    #         raise ValidationError("Validation Error")
    
    def validate_username(self, username): # username form
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one")
        
    def validate_email(self, email): # email form
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField("Login")
    
class UpdateAccountForm(FlaskForm):
    username = StringField("Username Here", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators = [FileAllowed(["jpg", "jpeg", "png"])])
    
    submit = SubmitField("Update")
    
    # Registration form checked if username or email exists, and throwing ValidationError if they were taken. Here, user can submit form without changing username or email, and that will still be valid. If I query database, I'll get ValidationError since username and email already taken. So, only run validation checks if data submitted is different than current username or email
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken. Please choose a different one")
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken. Please choose a different one")