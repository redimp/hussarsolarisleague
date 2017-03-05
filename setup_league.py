#!/usr/bin/env python
# coding=utf-8

"""
 This is ugly and hacked. Will probably be enhanced in the future.
"""

import random
import bcrypt
import sys
import operator
from hsl.models import User, Chassis, Hangar, Game
from hsl import db


def mk_pairs(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

# see http://stackoverflow.com/questions/11245746/league-fixture-generator-in-python

def fixtures(teams):
    if len(teams) % 2:
        teams.append('DAY OFF')  # if team number is odd - use 'day off' as fake team
    rotation = list(teams)       # copy the list
    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
    return fixtures

names_group0 = """Stewon
Divisibility
Bjoern Jorgensson
Batian
Thrawn372
Phellan Kell
axerion
Camron Lyraus
ShalaLottle
Hase36"""

names_group1 = """Eiswolf
George Pryde
SeekanDestroy
Justifier
Justin
AA-Ace
Wormflush
Red Imp
pabscht
XXX"""


group0, group1 = [], []

chassisname = [str(x.name).replace(' ','') for x in Chassis.query.all()]

def get_user(name):
    global chassisnames
    password = "%s%04i" % (random.choice(chassisname),random.randint(0,9999))
    print "%s\t%s" % (name, password)
    pwhash = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt(12))
    user = User(name,pwhash,'')
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(username=name).first()
    return user


for name in names_group0.strip().split("\n"):
    # create user
    u = get_user(name)
    group0.append(u)

for name in names_group1.strip().split("\n"):
    # create user
    group1.append(get_user(name))

for group in [group0, group1]:
    matches = fixtures(group)
    for dayc,f in enumerate(matches):
        n = len(f)
        matchlist = zip(f[0:n / 2], reversed(f[n / 2:n]))

        for match in matchlist:
            h, a = match
            xgame = Game()
            xgame.player_home_id = h.id
            xgame.player_away_id = a.id
            xgame.day = dayc * 2 + 1
            db.session.add(xgame)
            #print xgame
            xgame = Game()
            xgame.player_home_id = a.id
            xgame.player_away_id = h.id
            xgame.day = dayc * 2 + 2
            db.session.add(xgame)
            #print xgame
        print ""


    #print len(group), len(matches), sum([group[0] in x for x in matches])

db.session.commit()
#maps = """Forest Colony
#Frozen City
#Caustic Valley
#River City
#Frozen City Night
#Alpine Peaks
#Tourmaline Desert
#Canyon Network
#Terra Therma
#Crimson Strait
#HPG Manifold
#The Mining Collective
#Viridian Bog
#Polar Highlands
#Grim Plexus
#1v1 Test
#2v2 Test
#4v4 Test A
#4v4 Test B"""

#print maps.strip().split("\n")