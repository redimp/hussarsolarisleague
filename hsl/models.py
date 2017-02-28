"""

 models.py -- contains all the database models of the hsl application

"""

from hsl import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(64), unique=True , index=True)
    password = db.Column('password' , db.String(64))
    email = db.Column('email',db.String(64),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Setting(db.Model):
    __tablename__ = "settings"
    username = db.Column('name', db.String(64), unique=True , index=True, primary_key=True)
    password = db.Column('value' , db.String(64))
