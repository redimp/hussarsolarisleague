#!/usr/bin/env python
# coding=utf-8

import random
import operator
from hsl.models import User, Chassis, Hangar, Game


def mk_pairs(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

def fixtures(teams):
    if len(teams) % 2:
        teams.append('DAY OFF')  # if team number is odd - use 'day off' as fake team

    rotation = list(teams)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures

group0 = """Stewon
Divisibility
Bjoern Jorgensson
Batian
Thrawn372
Phellan Kell
axerion
Camron Lyraus
ShalaLottle
Hase36
"""

group1 = """Eiswolf
George Pryde
SeekanDestroy
Justifier
Justin
AA-Ace
Wormflush
Red Imp
pabscht"""


for group in [group0, group1]:
    group = group.strip().split("\n")
    #print len(group), group

    matches = mk_pairs(group)
    random.shuffle(matches)

    for pair in matches:
        pass
        #print pair

    matches = fixtures(group)
    for day,f in enumerate(matches):
        matchlist = zip(*[iter(f)] * 2)
        for match in matchlist:
            h, a = match
            print day * 2 + 1, h, a
            print day * 2 + 2, a, h

    #print len(group), len(matches), sum([group[0] in x for x in matches])


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