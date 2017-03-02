"""

 models.py -- contains all the database models of the hsl application

"""

import bcrypt
from datetime import datetime
from hsl import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), unique=True, index=True)
    password = db.Column('password', db.String(64))
    email = db.Column('email',db.String(64), unique=True, index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    in_group = db.Column('in_group', db.Integer, default=0)
    has_premium = db.Column('has_premium', db.Boolean, default=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password.encode('utf8'), self.password.encode('utf8'))
        return self.password == pwhash

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
    username = db.Column('name', db.String(64), unique=True, index=True, primary_key=True)
    password = db.Column('value', db.String(64))


class Chassis(db.Model):
    __tablename__ = "chassis"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    weight = db.Column('weight', db.Integer)
    weightclass = db.Column('class', db.Enum('Light','Medium','Heavy','Assault'))
    trial_available = db.Column('trial_available', db.Boolean, default=False)


class Hangar(db.Model):
    __tablename__ = "hangar"
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chassis_id = db.Column(db.Integer, db.ForeignKey('chassis.id'))
    available = db.Column('available', db.Integer)
    used = db.Column('used', db.Integer, default = 0)
    trial = db.Column('trial', db.Boolean)
    # Relationships
    chassis = db.relationship('Chassis', foreign_keys=chassis_id)
    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, user_id, chassis_id, trial=False):
        self.user_id = user_id
        self.chassis_id = chassis_id
        self.trial = trial
        self.available = 1
        self.used = 0

    def is_available(self):
        return self.trial or self.used < self.available
