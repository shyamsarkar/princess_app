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
    createdate = db.Column(db.Date, nullable=False, server_default=func.now())
    createtime = db.Column(db.Time, nullable=False, server_default=func.now())
    lastupdated = db.Column(db.Date, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    updatetime = db.Column(db.Time, nullable=False,
                           server_default=func.now(), onupdate=func.now())


class Income_group(Actionclass):
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    ipaddress = db.Column(db.String(30), nullable=False)
    createdby = db.Column(db.Integer, nullable=False)
    createdate = db.Column(db.Date, nullable=False, server_default=func.now())
    createtime = db.Column(db.Time, nullable=False, server_default=func.now())
    lastupdated = db.Column(db.Date, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    updatetime = db.Column(db.Time, nullable=False,
                           server_default=func.now(), onupdate=func.now())


class Expense_group(Actionclass):
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    ipaddress = db.Column(db.String(30), nullable=False)
    createdby = db.Column(db.Integer, nullable=False)
    createdate = db.Column(db.Date, nullable=False, server_default=func.now())
    createtime = db.Column(db.Time, nullable=False, server_default=func.now())
    lastupdated = db.Column(db.Date, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    updatetime = db.Column(db.Time, nullable=False,
                           server_default=func.now(), onupdate=func.now())


class Income_Entry(Actionclass):
    income_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, nullable=True)
    income_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    remark = db.Column(db.String(100), nullable=False)
    ipaddress = db.Column(db.String(30), nullable=False)
    createdby = db.Column(db.Integer, nullable=False)
    createdate = db.Column(db.Date, nullable=False, server_default=func.now())
    createtime = db.Column(db.Time, nullable=False, server_default=func.now())
    lastupdated = db.Column(db.Date, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    updatetime = db.Column(db.Time, nullable=False,
                           server_default=func.now(), onupdate=func.now())


class Expense_Entry(Actionclass):
    expense_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, nullable=True)
    expense_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    remark = db.Column(db.String(100), nullable=False)
    ipaddress = db.Column(db.String(30), nullable=False)
    createdby = db.Column(db.Integer, nullable=False)
    createdate = db.Column(db.Date, nullable=False, server_default=func.now())
    createtime = db.Column(db.Time, nullable=False, server_default=func.now())
    lastupdated = db.Column(db.Date, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    updatetime = db.Column(db.Time, nullable=False,
                           server_default=func.now(), onupdate=func.now())
