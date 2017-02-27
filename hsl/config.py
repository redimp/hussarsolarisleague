import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'hsl.sqlite')
SECRET_KEY = 'ied8Wohquoovielee8yae0aip3pef1th'
SQLALCHEMY_TRACK_MODIFICATIONS = False
