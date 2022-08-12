from models import *
from auth.urls import auth
from mobileapp.urls import mobileapp


""" Setting user_id in session by flask login """
"""  
.\venv\Scripts\activate
$env:flask_app="app"
$env:flask_env="development"
flask run
"""


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


""" Blueprint App urls.py registration """

app.register_blueprint(auth)
app.register_blueprint(mobileapp)


""" Flask and Flask-SQLAlchemy initialization here """


""" flask script will come here """


# Very Basic App Definition


@app.route('/')
def index():
    # return render_template("index.html")
    return redirect(url_for('auth.index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')

if __name__=="__main__":
    app.run()

