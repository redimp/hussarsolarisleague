from hsl import app, db
from flask import render_template, request, session, request, \
                  flash, url_for, redirect, render_template, abort, g
from flask_login import login_user, logout_user, current_user, login_required
import re
import bcrypt
from hsl.models import User, Chassis, Hangar
from hsl.rules import check_hangar_for_errors


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
    elif re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                  request.form["email"]) is None:
        error = "Email looks invalid to me."

    if User.query.filter_by(username=request.form['username'])\
           .first() is not None:
        error = "Username is already taken."
    if User.query.filter_by(email=request.form['email']).first() is not None:
        error = "eMail Adress is already taken."

    if error is not None:
        flash(error, 'error')
        return render_template('register.html')

    pwhash = bcrypt.hashpw(request.form['password'].encode('utf8'),
                           bcrypt.gensalt(12))
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
    if registered_user is None or \
            not registered_user.verify_password(password):
        flash('Username or Password is invalid.', 'error')
        return redirect(url_for('login'))

    login_user(registered_user)
    flash('Logged in successfully.', 'success')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    flash('Good bye.')
    return redirect(url_for('index'))


@app.route('/hangar', methods=['GET', 'POST'])
@login_required
def hangar():
    current_hangar = Hangar.query.filter_by(user_id=g.user.get_id())\
                     .join(Chassis)\
                     .order_by(Chassis.weight).all()
    if len(current_hangar) < 1:
        return redirect(url_for('setup_hangar'))
    return render_template("hangar.html", current_hangar=current_hangar)


@app.route('/games', methods=['GET', 'POST'])
@login_required
def games():
    return render_template("games.html")


@app.route('/setup_hangar', methods=['GET', 'POST'])
@login_required
def setup_hangar():
    current_hangar = Hangar.query.filter_by(user_id=g.user.get_id()).all()
    if len(current_hangar) > 0:
        return redirect(url_for('hangar'))

    chassis = Chassis.query.all()

    # prevent dirty tricks
    selected_mechs = list(set([int(x) for x in request.form.getlist("mech")]))
    selected_trials = list(set([int(x) for x in request.form.getlist("trial")]))

    if (len(selected_trials) + len(selected_mechs)) > 0:
        mechs = Chassis.query.filter(Chassis.id.in_(selected_mechs)).all()
        trials = Chassis.query.filter(db.and_(Chassis.trial_available, Chassis.id.in_(selected_trials))).all()
        # prevent dirty tricks
        selected_mechs = [m.id for m in mechs]
        selected_trials = [m.id for m in trials]
        # check rules
        errors = check_hangar_for_errors(mechs, trials)
        if errors is None:
            # store hangar
            for mech_id in selected_mechs:
                hangar_mech = Hangar(user_id=g.user.get_id(), chassis_id=mech_id, trial=False)
                db.session.add(hangar_mech)
            for mech_id in selected_trials:
                hangar_mech = Hangar(user_id=g.user.get_id(), chassis_id=mech_id, trial=True)
                db.session.add(hangar_mech)
            db.session.commit()
            return redirect(url_for('hangar'))
        else:
            for error in errors:
                flash(error, 'error')

    return render_template("setup.html",
                           chassis=chassis,
                           selected_mechs=selected_mechs,
                           selected_trials=selected_trials)
