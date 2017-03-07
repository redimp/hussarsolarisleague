#!/usr/bin/env python

import os
import sys
from hsl.models import Game, User, Hangar
from hsl import db

users_total = User.query.count()

users_with_hangar = Hangar.query\
                 .join(User).group_by(User.id).count()

games_running = Game.query.filter_by(status=2).count()
games_finished = Game.query.filter_by(status=3).count()

print "Users total:", users_total
print "Users with a hangar:", users_with_hangar
print "Games running:", games_running
print "Games finished:", games_finished
