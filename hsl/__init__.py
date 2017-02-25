from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hsl.config')
db = SQLAlchemy(app)
from hsl import views
