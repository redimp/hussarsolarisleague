#!/usr/bin/env python
# coding=utf-8

"""
 This script sets a user password.

 e.g. $ ./set_password.py ["Exact Username"] <password>

"""

import random
import sys
import argparse
from hsl.models import User, Chassis
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
    parser.add_argument("username", help="name of the user", type=str)
    parser.add_argument("--password", '-p', help="password", type=str, required=False)
    args = parser.parse_args()

    username = args.username
    password = args.password or generate_password()

    user = User.query.filter_by(username=username).first()

    if user is None:
        print "User '%s' not found." % username
    else:
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        if args.password:
            print "Password updated."
        else:
            print "New password:", password

