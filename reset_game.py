#!/usr/bin/env python
# vim:set sts=4 ts=4 tw=78 sw=4 et ai:
# coding=utf-8

"""
 This script resets a given game.

 e.g. $ ./reset_game.py [id]

"""

import random
import sys
import argparse
from hsl.models import Game, Hangar
from hsl import db

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Reset a Game")
    parser.add_argument("id", help="number of the day", type=int, nargs='+')
    parser.add_argument("--verbose", "-v", help="verbose mode", action='store_true')
    args = parser.parse_args()

    games = Game.query.filter(Game.id.in_(args.id)).all()

    for current_game in games:
        print current_game
        # mark mechs as used
        mechs = Hangar.query.filter(Hangar.id.in_([current_game.mech_away_id,current_game.mech_home_id])).all()
        for m in mechs:
            m.used -= 1
            print '   ',m
            db.session.add(m)
        current_game.mech_away_id = None
        current_game.mech_home_id = None
        current_game.ready_home = None
        current_game.ready_away = None
        current_game.winner = None
        current_game.winner_home = None
        current_game.winner_away = None
        current_game.mech_home_id = None
        current_game.mech_away_id = None
        current_game.variant_home = None
        current_game.variant_away = None
        current_game.map = None
        current_game.status = 1
        db.session.add(current_game)

    db.session.commit()
