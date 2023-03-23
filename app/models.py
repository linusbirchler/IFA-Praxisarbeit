#Eigenentwicklung
from app import login
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for

#Übernommen
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#Eigenentwicklung
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
                'id': self.id,
                'username': self.username,
                '_links': {
                    'self': url_for('get_users', id=self.id)
                    }
                }
        if include_email:
            data['email'] = self.email
        return data

    def to_collection():
        users = User.query.all()
        data = {'items': [item.to_dict() for item in users]}
        return(data)

    def __repr__(self):
        return '<User {}>'.format(self.username)

#Eigenentwicklung
class Cleaning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    adresse = db.Column(db.String(64), index=True)
    wohnung = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    bemerkung = db.Column(db.String(255), index=True)

    def to_dict(self):
        data2 = {
                'name': self.name,
                'adresse': self.adresse,
                'wohnung': self.wohnung,
                'status': self.status,
                'bemerkung': self.bemerkung,
                '_links': {
                    'self': url_for('get_cleaning', id=self.id)
                    }
                }
        return data2
    
    def to_collection():
        clean = Cleaning.query.all()
        data2 = {'items': [item.to_dict() for item in clean]}
        return(data2)

    def __repr__(self):
        return '<cleaning {}>'.format(self.body)
