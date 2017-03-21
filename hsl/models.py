"""

 models.py -- contains all the database models of the hsl application

"""

import bcrypt
from datetime import datetime
from hsl import db
from flask import g


class User(db.Model):
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), unique=True, index=True)
    password = db.Column('password', db.String(64))
    #email = db.Column('email',db.String(64), unique=True, index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
    in_group = db.Column('in_group', db.Integer, default=0)
    has_premium = db.Column('has_premium', db.Boolean, default=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        #self.email = email
        self.registered_on = datetime.utcnow()

    def verify_password(self, password):
        pwhash = bcrypt.hashpw(password.encode('utf8'), self.password.encode('utf8'))
        return self.password == pwhash

    def set_password(self, password):
        self.password = bcrypt.hashpw(
                            password.encode('utf8'),
                            bcrypt.gensalt(12)
                            )

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
    name = db.Column('name', db.String(64), unique=True, index=True, primary_key=True)
    value = db.Column('value', db.String(64))

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Chassis(db.Model):
    __tablename__ = "chassis"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    weight = db.Column('weight', db.Integer)
    weightclass = db.Column('class', db.Enum('Light','Medium','Heavy','Assault'))
    trial_available = db.Column('trial_available', db.Boolean, default=False)

    def __repr__(self):
        return '<Chassis #%i %s>' % (self.id, self.name)


class Variant(db.Model):
    __tablename__ = "variant"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    chassis_id = db.Column('chassis_id',db.Integer, db.ForeignKey('chassis.id'))
    chassis = db.relationship('Chassis', foreign_keys=chassis_id)


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

    def __repr__(self):
        return '<Hangar #%i %s>' % (self.id, self.chassis.name)

class Game(db.Model):
    Maps = ['Forest Colony', 'Frozen City', 'Caustic Valley', 'River City',
            'Frozen City Night', 'Alpine Peaks', 'Tourmaline Desert',
            'Canyon Network', 'Terra Therma', 'Crimson Strait',
            'HPG Manifold', 'The Mining Collective', 'Viridian Bog',
            'Polar Highlands', 'Grim Plexus']
    Stati = ['Upcoming','Ready to begin','Running','Finished']
    id = db.Column('id', db.Integer, primary_key=True)
    day = db.Column('day', db.Integer)
    player_home_id = db.Column('player_home', db.Integer, db.ForeignKey('user.id'), index = True)
    player_away_id = db.Column('player_away', db.Integer, db.ForeignKey('user.id'), index = True)
    ready_home = db.Column('ready_home', db.Boolean)
    ready_away = db.Column('ready_away', db.Boolean)
    winner = db.Column('winner', db.Integer, db.ForeignKey('user.id'), nullable=True)
    winner_home = db.Column('winner_home', db.Integer, db.ForeignKey('user.id'), nullable=True)
    winner_away = db.Column('winner_away', db.Integer, db.ForeignKey('user.id'), nullable=True)
    mech_home_id = db.Column('mech_home_id', db.Integer, db.ForeignKey('hangar.id'), nullable=True)
    mech_away_id = db.Column('mech_away_id', db.Integer, db.ForeignKey('hangar.id'), nullable=True)
    variant_home = db.Column('variant_home', db.String(24), nullable=True)
    variant_away = db.Column('variant_away', db.String(24), nullable=True)
    map = db.Column('map', db.String(24), nullable=True)
    status = db.Column('status', db.Integer, nullable=False, default=0)
    # Relationships
    player_home = db.relationship('User', foreign_keys=player_home_id)
    player_away = db.relationship('User', foreign_keys=player_away_id)
    mech_home = db.relationship('Hangar', foreign_keys=mech_home_id)
    mech_away = db.relationship('Hangar', foreign_keys=mech_away_id)

    def get_status(self):
        s = self.Stati[self.status]
        if s == "Finished":
            if self.winner == g.user.id:
                return "Win"
            else:
                return "Loss"
        return s

    def get_opponent_info(self):
        if self.player_home_id == g.user.id:
            return (self.ready_away, self.mech_away_id,
                    self.mech_away.chassis if self.mech_away else "", self.player_away,
                    self.variant_away)
        else:
            return (self.ready_home, self.mech_home_id,
                    self.mech_home.chassis if self.mech_home else "", self.player_home,
                    self.variant_home)

    def get_info(self):
        if self.player_home_id == g.user.id:
            return (self.ready_home, self.mech_home_id,
                    self.mech_home.chassis if self.mech_home else "",
                    self.variant_home)
        else:
            return (self.ready_away, self.mech_away_id,
                    self.mech_away.chassis if self.mech_away else "",
                    self.variant_away)

    def __repr__(self):
        return '<Game #%i %s vs %s>' % (self.id, self.player_home.username, self.player_away.username)

def _string_cast_helper(value):
    if value is None: return None
    if value.lower() == "true": return True
    if value.lower() == "false": return False
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
                pass
    return value

def get_db_setting(name):
    entry = Setting.query.filter_by(name=name).first()
    if entry is None: return None
    return _string_cast_helper(entry.value)

def set_db_setting(name, value):
    entry = Setting.query.filter_by(name=name).first()
    if entry is None:
        entry = Setting(name=name, value=value)
    else:
        entry.value = value
    db.session.add(entry)
    db.session.commit()
