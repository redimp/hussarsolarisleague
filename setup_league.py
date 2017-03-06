#!/usr/bin/env python
# coding=utf-8

"""
 This script creates users and matches for groups given in .txt files.

 e.g. $ ./setup_league.py group1.txt group2.txt
 Potatoe                Archer5625
 Tomato                 Thunderbolt0766
 ...

"""

import random
import bcrypt
import sys
import operator
import argparse
from hsl.models import User, Chassis, Hangar, Game
from hsl import db


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

def get_user(name):
    global chassisnames
    password = "%s%04i" % (random.choice(chassisname),random.randint(0,9999))
    print "%-24s\t%s" % (name, password)
    pwhash = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt(12))
    user = User(name,pwhash,'')
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(username=name).first()
    return user

# passwords should be simple, yeah, thats
# biased like hell, but security doesnt really matter.
chassisname = [str(x.name).replace(' ','') for x in Chassis.query.all()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Setup League")
    parser.add_argument("files", help="One text file per group. One name per line.", type=str, nargs="+")
    args = parser.parse_args()

    for filename in args.files:
        with open(filename, 'r') as f:
            group_str = f.read()

        group = []
        
        for name in group_str.strip().split("\n"):
            # create user
            u = get_user(name)
            group.append(u)

        if len(group) < 0:
            print "Error no group found."

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

    db.session.commit()
