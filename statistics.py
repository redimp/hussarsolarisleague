#!/usr/bin/env python

import os
import sys
import operator
from hsl.models import Game, User, Hangar
from hsl import db

users_total = User.query.count()

users_with_hangar = Hangar.query\
                 .join(User).group_by(User.id).count()

games_running = Game.query.filter_by(status=2).count()
games_finished = Game.query.filter_by(status=3).count()
games_total = Game.query.count()

mechs_in_hangar = Hangar.query.count()
trials_in_hangar = Hangar.query.filter_by(trial=True).count()

print "Users total:", users_total
print "Users with a hangar:", users_with_hangar
print "Games running:", games_running
print "Games finished:", games_finished
print "Games total:", games_total
print "Mechs in Hangar:", mechs_in_hangar
print "Trials in Hangar:", trials_in_hangar

# tonnage information
usedTonnage = sum([game.mech_home.chassis.weight + game.mech_away.chassis.weight\
                   for game in Game.query.filter_by(status=3).all()])
totalTonnage = sum([mech.chassis.weight for mech in Hangar.query.all()])

print "Tonnage used (average): %d (%.2f)" % (usedTonnage, round(usedTonnage/2.0/games_finished,2))
print "Tonnage total (average): %d (%.2f)" % (totalTonnage, round(totalTonnage/mechs_in_hangar,2))

# win/loss ratio per tonnage
games = Game.query.filter_by(status=3).all()
wlPerTonnage = dict.fromkeys(range(20,101,5), 0.0+0.0j)
for game in games:
    # home is winner
    if game.winner == game.player_home_id:
        wlPerTonnage[game.mech_home.chassis.weight] += complex(1.0, 0.0)
        wlPerTonnage[game.mech_away.chassis.weight] += complex(0.0, 1.0)
    # away is winner
    else:
        wlPerTonnage[game.mech_away.chassis.weight] += complex(1.0, 0.0)
        wlPerTonnage[game.mech_home.chassis.weight] += complex(0.0, 1.0)

scorePerTonnage = dict.fromkeys(range(20,101,5), (0.0, 0.0, 0.0))
for tonnage, value in wlPerTonnage.iteritems():
    if abs(value) > 0.0:
        scorePerTonnage[tonnage] = (value.real/(value.real+value.imag), value.real, value.imag)
scorePerTonnage = sorted(scorePerTonnage.items(), key=operator.itemgetter(1), reverse=True)

print "\nTonnage\t\tWin/Loss\tWin\tLoss"
for tonnage, value in scorePerTonnage:
    print "%3d\t\t%6.2f\t\t%2d\t%3d" % (tonnage, value[0], value[1], value[2])

weightsAll = {}
for user in User.query.all():
    # user is home
    game_home = Game.query.filter_by(status=3,player_home_id = user.id).all()
    weightsOwn = [game.mech_home.chassis.weight for game in game_home]
    weightsEnemy = [game.mech_away.chassis.weight for game in game_home]

    # user is away
    game_away = Game.query.filter_by(status=3,player_away_id = user.id).all()
    weightsOwn += [game.mech_away.chassis.weight for game in game_away]
    weightsEnemy += [game.mech_home.chassis.weight for game in game_home]
    if len(weightsOwn) > 0 and len(weightsEnemy) > 0:
        weightsAll[user.username] = (sum(weightsOwn), sum(weightsEnemy))

weightsAll = sorted(weightsAll.items(), key=operator.itemgetter(0), reverse=False)

print "\n%-20s\t%s\t%s\t\t%s" % ("Player", "Tonnage (own)", "Tonnage (enemy)", "Difference")
for user, value in weightsAll:
    print "%-20s\t%8d\t%8d\t\t%+6d" % (user, value[0], value[1], value[1]-value[0])
