#Eigenentwicklung
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'IFA2023'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cleaning:IFA2023@localhost/cleaning'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
