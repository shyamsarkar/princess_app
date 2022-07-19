from models import *

mobileapp = Blueprint('mobileapp', __name__, url_prefix='/mobileapp',
                      template_folder='templates',
                      static_folder='static', static_url_path='/')


@mobileapp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@mobileapp.route('income_group', methods=['GET', 'POST'])
@login_required
def income_group():
    return render_template('income_group.html')


@mobileapp.route('income_entry', methods=['GET', 'POST'])
@login_required
def income_entry():
    return render_template('income_entry.html')
