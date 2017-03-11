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

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Enable Gameday")
    parser.add_argument("day", help="number of the day", type=int)
    parser.add_argument("--verbose", "-v", help="verbose mode", action='store_true')
    args = parser.parse_args()

    games = Game.query.filter_by(day=args.day, status=0).all()

    for x in games:
        if args.verbose: print x
        x.status = 1
        db.session.add(x)
    db.session.commit()
    print "%i games on day %i enabled." % (len(games),args.day)
