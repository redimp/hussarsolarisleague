#!/usr/bin/env python

import os
import sys
from hsl.models import Game, User, Hangar, Chassis
from hsl import db

for u in User.query.all():
	l = Hangar.query.join(Chassis).filter(db.and_(Hangar.user_id == u.id, Chassis.weightclass == "Light")).count()
	m = Hangar.query.join(Chassis).filter(db.and_(Hangar.user_id == u.id, Chassis.weightclass == "Medium")).count()
	h = Hangar.query.join(Chassis).filter(db.and_(Hangar.user_id == u.id, Chassis.weightclass == "Heavy")).count()
	a = Hangar.query.join(Chassis).filter(db.and_(Hangar.user_id == u.id, Chassis.weightclass == "Assault")).count()
	print "%-20s %i %i %i %i" % (u.username, l, m, h, a)
