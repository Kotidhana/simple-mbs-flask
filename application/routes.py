from flask import Flask, render_template, request, redirect, url_for, flash, session
from application import app
from os import abort
from application.models import Customer,Medicine,Order

@app.route('/')
def index():
    return render_template('index.html',login=True)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():

    if request.method=='POST':
        return render_template('register.html')
    else:
        return redirect(url_for('home'))

@app.route('/dashboard', methods=['GET','POST'])
def manage():
    if request.method=='POST':
        flash('Welcome...')
        return render_template('dashboard.html')
    else:
        return redirect('/')
     
@app.route('/contact')
def about():
    # return render_template('about.html')
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'),404
    