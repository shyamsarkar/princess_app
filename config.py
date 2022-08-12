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

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/princess_app'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/princess_app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wpcmhuddtrvcdo:fdc9b774f26e3012e8734d51d58adfee5a1e3007337cd5f19138c970a3a2b73d@ec2-34-234-240-121.compute-1.amazonaws.com:5432/dc86t460v6iiu8'
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
