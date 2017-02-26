from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('hsl.config')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

from hsl import views, models

db.create_all()

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

