from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo,Length,Email,ValidationError
from application.models import Customer
class LoginForm(FlaskForm):
    user_id     =   StringField("User ID", validators=[DataRequired()])
    password    =   PasswordField("Password", validators=[DataRequired()])
    submit      =   SubmitField()

class RegisterForm(FlaskForm):
    f_name      =   StringField("Full Name", validators=[DataRequired()])
    phone       =   IntegerField("Phone number", validators=[DataRequired()])
    mail        =   StringField("Email ID", validators=[DataRequired()])
    p_name      =   StringField("Pharmacy Name", validators=[DataRequired()])
    addr        =   StringField("Pharmacy Address", validators=[DataRequired()])
    city        =   StringField("City", validators=[DataRequired()])
    state       =   StringField("State", validators=[DataRequired()])
    pincode     =   IntegerField("Pincode", validators=[DataRequired()])
    li_no       =   StringField("Licence Number", validators=[DataRequired()])
    user_id     =   StringField("Username", validators=[DataRequired()])
    password    =   PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    c_password  =   PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15),EqualTo('password')])
    submit      =   SubmitField()

    def validate_email(self, mail):
        cust = Customer.objects(mail=mail.data).first()
        if cust:
            raise ValidationError('Email is Already in use, Please pick Another.')