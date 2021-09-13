from flask import render_template, url_for, flash, redirect
from src import app, db, bcrypt
from src.forms import RegistrationForm, LoginForm, PlayGame
#from dictionaries import Dict
from flask_login import login_user, current_user, logout_user, login_required
from src.models import User, Scores#, Levels
from sqlalchemy.orm import aliased
from sqlalchemy import desc, func
password_hash=[]

@app.route("/")
def empy():
    return render_template('index.html')
@app.route("/home")
@login_required
def home():
    #levels = Scores.query.all()
    users = db.session.query(User.username)
    #user = User.query.get(username)
    for user in users:
         users = user.username
    return render_template('home.html', user=users)


@app.route("/<username>")
@login_required
def about(username):
    user = User.query.get(username)
    return render_template('about.html', title='About', username=username,user=user, password=password_hash)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        #flash(f'Account created for {form.username.data}!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/post/game', methods=['GET', 'POST'])
@login_required
def game():
    form = PlayGame()
    if form.validate_on_submit():
        level = Scores(level=form.level.data,level_score=form.score.data, useru=current_user)
        #levelscore= Levels(scores=scoresu)
        db.session.add(level)
        #db.session.add(levelscore)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('game.html', form=form)


@app.route('/<int:levels>/scores')
@login_required
def lscores(levels):
    #ab = user
    users = current_user.username
    ab = db.session.query(User.username,func.max(Scores.level_score)).filter(Scores.user_id == User.id)\
        .where(Scores.level==levels).where(User.username==users).all()
    #if level in ab:
        #ab = user[users][level][levels]
    return render_template("inds.html",users=users, levels=levels, ab=ab, abc=users)


@app.route('/<int:level>/allhighestscores')
@login_required
def hscores(level):
    ad = db.session.query(User.username,func.max(Scores.level_score)).filter(Scores.user_id == User.id)\
        .where(Scores.level==level).group_by(User.username).order_by(User.username).all()
    # ab = user
    #abd = level
   # users = user[]
    #ab = user[a]['level'][level]
    # if level in ab:
    # ab = user[users][level][levels]
    return render_template("high.html", level=level, ad=ad)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))