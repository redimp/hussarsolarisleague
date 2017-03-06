#!/usr/bin/env python
# coding=utf-8

"""
 This script enables a gameday.

 e.g. $ ./enable_gameday.py [day]

"""

import random
import sys
import argparse
from hsl.models import Game
from hsl import db

def generate_password():
    list = [str(x.name).replace(' ','') for x in Chassis.query.all()]
    if len(list)>8:
        prefix = random.choice(list)
    else:
        prefix = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(6))

    return "%s%04i" % (prefix,random.randint(0,9999))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Setup League")
    parser.add_argument("day", help="number of the day", type=int)
    parser.add_argument("--verbose", "-v", help="verbose mode", action='store_true')
    args = parser.parse_args()

    games = Game.query.filter_by(day=args.day, status=0).all()

    for x in games:
        if args.verbose: print x
        x.status = 1
        db.session.add(x)
    db.session.commit()
    print "%i games enabled." % len(games)