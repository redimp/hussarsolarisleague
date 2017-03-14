from hsl import app, db
from flask import render_template, request, session, request, \
                  flash, url_for, redirect, render_template, abort, g
from flask_login import login_user, logout_user, current_user, login_required
import hsl
from hsl.models import User, Chassis, Hangar, Game, get_db_setting
from hsl.rules import check_hangar_for_errors
import random


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
    if not app.config['REGISTER_ENABLED']:
        flash("Sign up is currently disabled.","warning")
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('register.html')
    error = None
    if len(request.form.get('username')) < 3:
        error = "Username too short."
    elif request.form.get('password') != request.form.get('repeat'):
        error = "Passwords do not match."
    #elif re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    #              request.form.get("email")) is None:
    #    error = "Email looks invalid to me."*/

    if User.query.filter_by(username=request.form.get('username'))\
           .first() is not None:
        error = "Username is already taken."
    #if User.query.filter_by(email=request.form.get('email')).first() is not None:
    #    error = "eMail Adress is already taken."

    if error is not None:
        flash(error, 'error')
        return render_template('register.html')

    user = User(request.form.get('username'), '', '')
    user.set_password(request.form.get('password'))
    db.session.add(user)
    db.session.commit()

    if app.config['TEST_MODE']:
        # mechs of test user 1
        test_mechs = []
        for x in Hangar.query.filter_by(user_id=1).all():
            test_mechs.append(x.id)

        # create test games
        for x in xrange(4):
            # hinspiel
            home_game = Game()
            home_game.day = x*2+1
            home_game.player_home_id = user.id
            home_game.player_away_id = 1
            home_game.ready_home = None
            home_game.ready_away = True
            home_game.winner = None
            home_game.winner_home =  None
            home_game.winner_away = user.id
            home_game.mech_home_id = None
            home_game.mech_away_id = random.choice(test_mechs)
            home_game.status = 1
            db.session.add(home_game)
            # rueckspiel
            away_game = Game()
            away_game.day = x*2+2
            away_game.player_home_id = 1
            away_game.player_away_id = user.id
            away_game.ready_home = True
            away_game.ready_away = None
            away_game.winner = None
            away_game.winner_home = 1
            away_game.winner_away = None
            away_game.mech_home_id = random.choice(test_mechs)
            away_game.mech_away_id = None
            away_game.status = 1
            db.session.add(away_game)

    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None or \
            not registered_user.verify_password(password):
        flash('Username or Password is invalid.', 'error')
        return redirect(url_for('login'))

    # check if [x] remember_me was set
    remember_me = 'remember_me' in request.form

    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully.', 'success')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template('profile.html')
    oldpassword = request.form.get('oldpassword')
    password = request.form.get('password')
    repeat = request.form.get('password')

    if request.form.get('update_premium'):
        g.user.has_premium = (len(request.form.getlist('premium'))>0)
        db.session.add(g.user)
        db.session.commit()
        flash('Premium Status updated', 'success')
    elif password and oldpassword and repeat and len(password + oldpassword + repeat) > 0:
        error = None
        if not g.user.verify_password(oldpassword):
            error = "The old password is invalid."
        if len(password)<3:
            error = "The new password is too short."
        if password != repeat:
            error = "Passwords do not match."
        elif oldpassword == password:
            error = "Old password and new password are the same."
        if error is None:
            # update hash
            g.user.set_password(password)
            db.session.add(g.user)
            db.session.commit()
            hsl.logmsg("password updated.")
            logout_user()
            flash('Password changed successfully.', 'success')
            return redirect(url_for('login'))
        if error is not None:
            flash(error,'error')
    return render_template('profile.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Good bye.')
    return redirect(url_for('index'))


@app.route('/hangar', methods=['GET', 'POST'])
@login_required
def hangar():
    current_hangar = Hangar.query.filter_by(user_id=g.user.id)\
                     .join(Chassis)\
                     .order_by(Chassis.weight).all()
    if len(current_hangar) < 1:
        return redirect(url_for('setup_hangar'))
    return render_template("hangar.html", current_hangar=current_hangar)


@app.route('/games', methods=['GET', 'POST'])
@login_required
def games():
    gamelist = Game.query.filter(
                db.or_(Game.player_home_id == g.user.id,
                       Game.player_away_id == g.user.id)
            ).order_by(Game.day).all()
    return render_template("games.html", games=gamelist)


@app.route('/game/<int:game_id>', methods=['GET', 'POST'])
@login_required
def game_detail(game_id):
    current_game = Game.query.filter_by(id=game_id).first()

    if current_game is None:
        abort(404)

    # check permissions
    if g.user.id not in [current_game.player_home_id, current_game.player_away_id]:
        flash("You have no permission to access %r" % current_game, 'error')
        return redirect(url_for('games'))

    # shortcut
    home_team = g.user.id == current_game.player_home_id

    if home_team:
        selected_mech, ready = current_game.mech_home_id, current_game.ready_home
        selected_winner = current_game.winner_home
    else:
        selected_mech, ready = current_game.mech_away_id, current_game.ready_away
        selected_winner = current_game.winner_away

    #print g.user, current_game, "Form", request.form, "ready", ready

    if request.method == 'POST':
        if current_game.status == 1:
            # Ready to begin
            selected_mech = int(request.form.get('mech') or 0)
            ready = True if request.form.getlist('ready') else False
            if ready and selected_mech == 0:
                flash('You have to select a mech to ready up.', 'warning')
                ready = False
            if ready:
                # mark all other games as unready
                other_games = Game.query.filter(Game.id != current_game.id, Game.player_home_id == g.user.id, Game.status == 1).all()
                for ogame in other_games:
                    ogame.ready_home = False
                    ogame.mech_home_id = None
                    db.session.add(ogame)
                other_games = Game.query.filter(Game.id != current_game.id, Game.player_away_id == g.user.id, Game.status == 1).all()
                for ogame in other_games:
                    ogame.ready_away = False
                    ogame.mech_away_id = None
                    db.session.add(ogame)
            if home_team:
                current_game.ready_home = ready
                current_game.mech_home_id = selected_mech
            else:
                current_game.ready_away = ready
                current_game.mech_away_id = selected_mech

            if current_game.ready_home and current_game.ready_away:
                # update status
                current_game.status = 2
                # roll map
                current_game.map = random.choice(Game.Maps)
                hsl.logmsg("%s set to status 2 map: %s" % (current_game,current_game.map))
                # mark mechs as used
                mechs = Hangar.query.filter(Hangar.id.in_([current_game.mech_away_id,current_game.mech_home_id])).all()
                for m in mechs:
                    m.used += 1
                    db.session.add(m)

            db.session.add(current_game)
            db.session.commit()

        if current_game.status == 2:
            winner = int(request.form.get('winner') or 0)
            if winner > 0:
                if home_team:
                    current_game.winner_home = winner
                    selected_winner = winner
                else:
                    current_game.winner_away = winner
                    selected_winner = winner

                if current_game.winner_home == current_game.winner_away:
                    # both sides decided a winner
                    current_game.winner = current_game.winner_away
                    # set new status
                    current_game.status = 3
                    hsl.logmsg("%s set to status 3 winner: %s" % (current_game, current_game.winner))

                db.session.add(current_game)
                db.session.commit()

    player_hangar = Hangar.query.filter(
            db.and_(Hangar.user_id == g.user.id,
                    db.or_(Hangar.available > Hangar.used, Hangar.trial)
                )
            ).join(Chassis).order_by(Chassis.weight, Chassis.name).all()

    return render_template("gamedetail.html", game=current_game, selected_winner=selected_winner,
                           hangar=player_hangar, selected_mech=selected_mech, ready=ready)


@app.route('/setup_hangar', methods=['GET', 'POST'])
@login_required
def setup_hangar():
    current_hangar = Hangar.query.filter_by(user_id=g.user.id).all()
    if len(current_hangar) > 0:
        return redirect(url_for('hangar'))

    chassis = Chassis.query.all()

    # prevent dirty tricks
    selected_mechs = list(set([int(x) for x in request.form.getlist("mech")]))
    selected_trials = list(set([int(x) for x in request.form.getlist("trial")]))
    everything_ok = False

    if (len(selected_trials) + len(selected_mechs)) > 0:
        if len(selected_mechs)>0:
            mechs = Chassis.query.filter(Chassis.id.in_(selected_mechs)).all()
        else:
            mechs = []
        if len(selected_trials)>0:
            trials = Chassis.query.filter(db.and_(Chassis.trial_available, Chassis.id.in_(selected_trials))).all()
        else:
            trials = []
        # prevent dirty tricks
        selected_mechs = [m.id for m in mechs]
        selected_trials = [m.id for m in trials]
        # check rules
        errors = check_hangar_for_errors(mechs, trials)
        if errors is None:
            everything_ok = True

            if len(request.form.getlist("confirmed"))>0:
                # store hangar
                for mech_id in selected_mechs:
                    hangar_mech = Hangar(user_id=g.user.id, chassis_id=mech_id, trial=False)
                    db.session.add(hangar_mech)
                for mech_id in selected_trials:
                    hangar_mech = Hangar(user_id=g.user.id, chassis_id=mech_id, trial=True)
                    db.session.add(hangar_mech)
                db.session.commit()
                hsl.logmsg("hangar setup done.")
                return redirect(url_for('hangar'))
        else:
            for error in errors:
                flash(error, 'error')

    return render_template("setup.html",
                           chassis=chassis,
                           selected_mechs=selected_mechs,
                           selected_trials=selected_trials,
                           everything_ok=everything_ok)

@app.route('/scoreboard/<int:day>')
@app.route('/scoreboard')
def scoreboard(day=None):
    gamedays = sorted(list(set([x.day for x in Game.query.filter(Game.status>0).group_by(Game.day).all()])))
    inactive_gamedays = sorted(list(set([x.day for x in Game.query.filter(Game.status == 0).group_by(Game.day).all()])))
    group_ids = sorted(list(set([x.in_group for x in User.query.all()])))
    # pick last day
    if day is None:
        day = gamedays[-1]

    #print gamedays

    # for each group collect games of the chosen day:
    groups_and_games = {}
    for gid in group_ids:
        games = Game.query.join(User,Game.player_home_id==User.id)\
            .filter(db.and_(Game.day==day,User.in_group == gid))\
            .order_by(User.username)\
            .all()
        groups_and_games[gid] = games

    #current_hangar = Hangar.query.filter_by(user_id=g.user.id)\
    #                 .join(Chassis)\
    #                 .order_by(Chassis.weight).all()

    #print groups_and_games

    return render_template("scoreboard.html", display_gameday=day, gamedays=gamedays, inactive_gamedays=inactive_gamedays, groups_and_games=groups_and_games)

