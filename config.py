from operator import and_
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_
from datetime import timedelta, datetime
import os
from sqlalchemy.sql import func
# flask login
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
# flask wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
# flask migrate
from flask_migrate import Migrate
# flask admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# flask script
# from flask_script import Manager, Command


# app Configuration
app = Flask(__name__, template_folder='templates', static_folder='static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/princess_app'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/princess_app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mwvdnaalpgpoaq:1d541ada3bf9901310effaad1a49206de4705dda0e029ec1c5bba7f8543bfb9b@ec2-34-203-182-65.compute-1.amazonaws.com:5432/dc2bcg4rjkap8m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = False
app.config['UPLOAD_FOLDER'] = '.\\static\\uploaded'
db = SQLAlchemy(app)
app.secret_key = 'This_is_a_very_complex_secret_key'
app.permanent_session_lifetime = timedelta(hours=24)


# Flask login configuration and initialization

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.index'
login_manager.login_message = "Please Enter Username and Password!"


# Flask Migrate
migrate = Migrate(app, db)


""" Flask Admin """
# admin = Admin(app, name='Administrator', template_mode='bootstrap4')


# Flask Script


# script_manager = Manager(app)
