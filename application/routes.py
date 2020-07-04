from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from application import app
from application.models import Customer,Medicine,Order
from application.forms import LoginForm,RegisterForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',login=True)


@app.route('/login', methods=['GET','POST'])
def login():
    lForm = LoginForm()
    if lForm.validate_on_submit():
        userid      =   request.form.get('userid')
        password    =   lForm.password.data

        user = Customer.objects(user_id=userid).first()
        if user and password==user.password:
            flash('Login Successful!','success')
            return redirect('/index')
    else:
        flash('Userid and Password Does not match!...Try again','danger')
    return render_template('login.html',form=lForm)



@app.route('/register', methods=['GET','POST'])
def register():
    rForm = RegisterForm()
    return render_template('register.html',form=rForm)


@app.route('/dashboard')
def manage():
    return render_template('dashboard.html')



@app.route('/contact')
def about():
    return render_template('about.html')
#     return abort(404)
@app.route('/<code>')
def not_found(code):
    return render_template('not_found.html',str=code)

    