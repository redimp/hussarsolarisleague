from hsl import app, db
from flask import render_template, request, session, request,\
                  flash, url_for, redirect, render_template, abort, g
from flask_login import login_user, logout_user, current_user, login_required
import re
import bcrypt
from hsl.models import User


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    error = None
    if len(request.form['username']) < 3:
        error = "Username too short."
    elif request.form['password'] != request.form['repeat']:
        error = "Passwords do not match."
    elif re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", request.form["email"]) is None:
        error = "Email looks invalid to me."

    if User.query.filter_by(username=request.form['username']).first() is not None:
        error = "Username is already taken."
    if User.query.filter_by(email=request.form['email']).first() is not None:
        error = "eMail Adress is already taken."

    if error is not None:
        flash(error, 'error')
        return render_template('register.html')

    pwhash = bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt(12))
    user = User(request.form['username'], pwhash, request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None or not registered_user.verify_password(password):
        flash('Username or Password is invalid.', 'error')
        return redirect(url_for('login'))

    login_user(registered_user)
    flash('Logged in successfully.','success')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    flash('Good bye.')
    return redirect(url_for('index'))


@app.route('/hangar', methods=['GET', 'POST'])
@login_required
def hangar():
    return render_template("hangar.html")


@app.route('/games', methods=['GET', 'POST'])
@login_required
def games():
    return render_template("games.html")
