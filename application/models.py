import flask
from application import db

class Customer(db.Document):
    cust_id =   db.IntField( unique=True )
    f_name  =   db.StringField( max_length=20 )
    l_name  =   db.StringField( max_length=20 )
    phone   =   db.IntField( max_length=12 )
    mail    =   db.StringField( max_length=20 )
    p_name  =   db.StringField( max_length=20 )
    addr_1  =   db.StringField( max_length=25 )
    addr_2  =   db.StringField( max_length=25 )
    city    =   db.StringField( max_length=20 )
    state   =   db.StringField( max_length=15 )
    pincode =   db.IntField( max_length=6 )
    li_no   =   db.StringField( max_length=10 )

class Medicine(db.Document):
    med_id  =   db.StringField( max_length=10, unique=True )
    m_name  =   db.StringField( max_length=20 )
    desc    =   db.StringField( max_length=255 )

class Order(db.Document):
    cust_id =   db.ObjectIdField()
    med_id  =   db.ObjectIdField()