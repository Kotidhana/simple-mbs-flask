import flask
from application import db
from werkzeug.security import generate_password_hash,check_password_hash

class Customers(db.Document):
    f_name  =   db.StringField( max_length=20 )
    phone   =   db.IntField( max_length=12 )
    mail    =   db.StringField( max_length=20 )
    p_name  =   db.StringField( max_length=20 )
    addr    =   db.StringField( max_length=25 )
    city    =   db.StringField( max_length=20 )
    state   =   db.StringField( max_length=15 )
    pincode =   db.IntField( max_length=6 )
    li_no   =   db.StringField( max_length=10 )
    password=   db.StringField()
    user_id =   db.StringField( max_length=20, unique=True )

    def set_password(self, password):
        self.password   =   generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)
    

class Medicine(db.Document):
    med_id  =   db.StringField( max_length=10, unique=True )
    m_name  =   db.StringField( max_length=20 )
    desc    =   db.StringField( max_length=255 )

class Order(db.Document):
    cust_id =   db.ObjectIdField()
    med_id  =   db.ObjectIdField()
