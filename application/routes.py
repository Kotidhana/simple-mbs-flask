from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from application import app,db
from application.models import Customers, Medicine, Order
from application.forms import LoginForm,RegisterForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',login=True, title='Homepage')


@app.route('/login', methods=['GET','POST'])
def login():
    lForm = LoginForm()
    if lForm.validate_on_submit():
        user_id     =   lForm.user_id.data
        password    =   lForm.password.data

        user = Customers.objects(user_id = user_id).first()
        if user and password==user.password:
            flash('Login Successful!','success')
            return redirect('/index')
        else:
            flash('Userid and Password Does not match!...Try again','danger')
    return render_template('login.html',form=lForm, title='Login')



@app.route('/register', methods=['GET','POST'])
def register():
    rForm = RegisterForm()
    return render_template('register.html',form=rForm, title='Register')


@app.route('/dashboard')
def manage():
    medlist =   Medicine.objects.order_by('+med_id')
    cust    =   Customers.objects.order_by('+f_name')
    return render_template('dashboard.html',mlist=medlist,names=cust, title='Dashboard')



@app.route('/about')
def about():
    return render_template('about.html', title='About')
#     return abort(404)
@app.route('/<code>')
def not_found(code):
    return render_template('not_found.html',str=code)