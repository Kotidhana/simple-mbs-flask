from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from application import app,db
from application.models import Customers, Medicine, Order
from application.forms import LoginForm,RegisterForm



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',login=True, title='Homepage')




@app.route('/register', methods=['GET','POST'])
def register():
    rForm = RegisterForm()
    if rForm.validate_on_submit():
        f_name      =   rForm.f_name.data
        phone       =   rForm.phone.data
        mail        =   rForm.mail.data
        p_name      =   rForm.p_name.data
        addr        =   rForm.addr.data
        city        =   rForm.city.data
        state       =   rForm.state.data
        pincode     =   rForm.pincode.data
        li_no       =   rForm.li_no.data
        user_id     =   rForm.user_id.data
        password    =   rForm.password.data
        
        existing_user  =   Customers.objects(user_id=user_id).first()
        if existing_user:
            flash('Username Already exists!','danger')
            return redirect(url_for('register'))
        
        else:
            cust        =   Customers(f_name=f_name, phone=phone, mail=mail, p_name=p_name, addr=addr, city=city, state=state, pincode=pincode, user_id=user_id)
            cust.set_password(password)
            cust.save()
            flash('You are Successfully registered!!!','success')
            return redirect(url_for('index'))

    return render_template('register.html',form=rForm, title='Register')




@app.route('/login', methods=['GET','POST'])
def login():
    lForm = LoginForm()
    if lForm.validate_on_submit():
        user_id     =   lForm.user_id.data
        password    =   lForm.password.data

        cust = Customers.objects(user_id = user_id).first()
        if cust and cust.get_password(password):
            flash('Login Successful!','success')
            session['user_id']=cust.user_id
            return redirect('/index')
        else:
            flash('Userid and Password Does not match!...Try again','danger')

    return render_template('login.html',form=lForm, title='Login')




@app.route('/order')
def order():
    medlist         =   Medicine.objects.order_by('+med_id')
    return render_template('orders.html',mlist=medlist, title='MedList')




@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    m_id    =   request.form.get('med_id')
    m_n     =   request.form['m_name']
    cust_id =   session['user_id']

    if m_id:
        ord = Order.objects(cust_id=cust_id,med_id=m_id).first()
        if ord:
            flash(f"You already Ordered { m_n }!",'warning')
            redirect( url_for('order') )

        else:
            Order(cust_id=cust_id,med_id=m_id).save()
            flash(f"Order on { m_n } placed!",'success')  

    meds    =   list( Customers.objects.aggregate(*[{
                                                    '$lookup': {
                                                        'from': 'order', 
                                                        'localField': 'user_id', 
                                                        'foreignField': 'cust_id', 
                                                        'as': 'm1'
                                                    }
                                                }, {
                                                    '$unwind': {
                                                        'path': '$m1', 
                                                        'preserveNullAndEmptyArrays': False
                                                    }
                                                }, {
                                                    '$lookup': {
                                                        'from': 'medicine', 
                                                        'localField': 'm1.med_id', 
                                                        'foreignField': 'med_id', 
                                                        'as': 'm2'
                                                    }
                                                }, {
                                                    '$unwind': {
                                                        'path': '$m2', 
                                                        'preserveNullAndEmptyArrays': False
                                                    }
                                                }, {
                                                    '$match': {
                                                        'user_id': cust_id
                                                    }
                                                }
                                            ]))

    return render_template('dashboard.html', title='Dashboard', meds=meds)




@app.route('/about')
def about():
    return render_template('about.html', title='About')
#     return abort(404)




@app.route('/<code>')
def not_found(code):
    return render_template('not_found.html',str=code)