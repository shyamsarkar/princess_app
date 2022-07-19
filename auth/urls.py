from models import *

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 template_folder='templates',
                 static_folder='static', static_url_path='assets')


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('mobileapp.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=request.form.get('username'),
                                     password=request.form.get('password')).first()
        if user:
            login_user(user, remember=True)
            return redirect(url_for('mobileapp.dashboard'))
    return render_template('login.html', form=form)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


@auth.route('/dashboard')
@login_required
def dashboard():
    return redirect(url_for('mobile.dashboard'))
