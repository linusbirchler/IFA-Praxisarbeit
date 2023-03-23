#Eigenentwicklung
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

#Übernommen
class LoginForm(FlaskForm):
    username = StringField('Benutzername:', validators=[DataRequired()])
    password = PasswordField('Passwort:', validators=[DataRequired()])
    remember_me = BooleanField('Angemeldet bleiben')
    submit = SubmitField('Anmelden')

class RegistrationForm(FlaskForm):
    username = StringField('Benutzername:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort:', validators=[DataRequired()])
    password2 = PasswordField(
            'Passwort erneut eingeben:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Benutzername wird bereits verwendet')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-Mail Adresse wird bereits verwendet')

#Eigenentwicklung
class CleaningForm(FlaskForm):
    id = StringField('ID')
    name = StringField('Nachname', validators=[DataRequired()])
    adresse = StringField('Adresse und Ort', validators=[DataRequired()])
    wohnung = StringField('Wohnungsbezeichnung', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Reinigung abgeschlosssen'), ('Reinigung nicht abgeschlossen')])
    bemerkung = StringField('Bemerkung')
    submit = SubmitField('Bestätigen')    
