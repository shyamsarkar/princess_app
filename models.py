from action import *

""" If Table or Column is added or deleted then run these commands :-
    1. flask db migrate -m "here column added comment"
    2. flask db upgrade                             (this will update the database)

 """


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[
                           InputRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=2, max=50)])


class Users(Actionclass, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    usertype = db.Column(db.String(10), nullable=False)
    enable = db.Column(db.String(20), nullable=False)
    createdby = db.Column(db.Integer, nullable=False)
    ipaddress = db.Column(db.String(30), nullable=False)
    createdate = db.Column(db.Date, nullable=False)
    lastupdated = db.Column(db.Date, nullable=False)
