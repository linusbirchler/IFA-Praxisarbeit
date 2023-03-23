#Eigenentwicklung
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm, CleaningForm
from app.models import User, Cleaning
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app import db

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    clean = Cleaning.query.all()
    return render_template('index.html', clean=clean)

#Übernommen
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Benutzername oder Passwort ist falsch.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Benutzername oder Passwort ist falsch.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)

#Eigenentwicklung
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#Übernommen
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Gratulation, Ihre Registrierung wurde erfolgreich abgeschlossen. Sie können sich nun anmelden!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


#Eigenentwicklung
@app.route('/cleaning', methods=['GET', 'POST'])
@login_required
def cleaning():
    form = CleaningForm()
    print(form.errors)
    if form.validate_on_submit():
        cleaning = Cleaning(name=form.name.data, adresse=form.adresse.data, wohnung=form.wohnung.data, status=form.status.data, bemerkung=form.bemerkung.data)
        db.session.add(cleaning)
        db.session.commit()
        flash('Die Reinigung wurde erfasst!')
        print(form.errors)
        return redirect(url_for('index'))
    return render_template('cleaning.html', title='Cleaning', form=form)


#Eigenentwicklung
@app.route('/edit/<id>', methods=['GET','POST'])
@login_required
def edit(id):
    cleaning = Cleaning.query.get(id) 
    form = CleaningForm()
    print(form.errors)
    if cleaning:
        if form.validate_on_submit():
            cleaning.name = form.name.data
            cleaning.adresse = form.adresse.data
            cleaning.wohnung = form.wohnung.data
            cleaning.status = form.status.data
            cleaning.bemerkung = form.bemerkung.data
            db.session.commit()
            flash('Die Änderungen wurden übernommen.')
            print(form.errors)
            return redirect(url_for('index'))
        return render_template('edit.html', title='Edit', form=form, id=id)
    else:
        flash('ID nicht gefunden.')
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    cleaning = Cleaning.query.get(id)
    form = CleaningForm()
    if cleaning:
        db.session.delete(cleaning)
        db.session.commit()
        flash('Der Eintrag wurde gelöscht.')
        return redirect(url_for('index'))
    else:
        flash('ID nicht gefunden.')
    return redirect(url_for('index'))

#Eigenentwicklung
@app.route('/auftrag', methods=['GET'])
def auftrag():
    return render_template('auftrag.html', title='Auftrag')
