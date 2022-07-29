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
    # return obj.show(request)
    form = FlaskForm()
    if form.validate_on_submit():
        group_id = obj.test_input(request.form.get('group_id'))
        group_name = obj.test_input(request.form.get('group_name'))
        if group_name != "":
            form_data = {
                "group_name": group_name,
                "createdby": current_user.id,
                "ipaddress": obj.ipaddress()
            }
            # return jsonify(form_data)
            if int(group_id) == 0:
                try:
                    lastid = Income_group.insert_record(**form_data)
                    return jsonify({"resp": lastid.group_id, "status": "success"})
                except:
                    return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})
            else:
                try:
                    lastid = Income_group.update_record(group_id, **form_data)
                    return jsonify({"resp": lastid.group_id, "status": "success"})
                except:
                    return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})

    return render_template('income_group.html', current_user=current_user, form=form)


@mobileapp.route('show_income_group', methods=['GET'])
@login_required
def show_income_group():
    sql = Income_group.query.all()
    return render_template('show_income_group.html', current_user=current_user, sql=sql)


@mobileapp.route('edit_income_group', methods=['GET'])
@login_required
def edit_income_group():
    id = obj.test_input(request.args.get('id'))
    rowedit = Income_group.query.get(int(id))
    return jsonify({"group_name": rowedit.group_name, "group_id": rowedit.group_id})


@mobileapp.route('delete_income_group', methods=['GET', 'POST'])
@login_required
def delete_income_group():
    # id = obj.test_input(request.args.get('id'))
    id = obj.test_input(request.form.get('id'))
    where = {"group_id": int(id)}
    try:
        deleted_id = Income_group.delete_record(**where)
        return jsonify({"resp": deleted_id, "status": "success"})
    except:
        return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})


@mobileapp.route('income_entry', methods=['GET', 'POST'])
@login_required
def income_entry():
    form = FlaskForm()
    if form.validate_on_submit():
        # return obj.show(request)
        income_id = obj.test_input(request.form.get('income_id'))
        group_id = obj.test_input(request.form.get('group_id'))
        income_date = obj.test_input(request.form.get('income_date'))
        amount = obj.test_input(request.form.get('amount'))
        remark = obj.test_input(request.form.get('remark'))
        if group_id != "" and income_date != "" and amount != "":
            form_data = {
                "group_id": group_id,
                "income_date": income_date,
                "amount": amount,
                "remark": remark,
                "createdby": current_user.id,
                "ipaddress": obj.ipaddress()
            }
            # return jsonify(form_data)
            if int(income_id) == 0:
                try:
                    lastid = Income_Entry.insert_record(**form_data)
                    return jsonify({"resp": lastid.income_id, "status": "success"})
                except:
                    return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})
            else:
                try:
                    lastid = Income_Entry.update_record(income_id, **form_data)
                    return jsonify({"resp": lastid.income_id, "status": "success"})
                except:
                    return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})
    qry_group = Income_group.query.all()
    return render_template('income_entry.html', form=form, qry_group=qry_group)


@mobileapp.route('show_income_entry', methods=['GET'])
@login_required
def show_income_entry():
    sql = Income_Entry.query.all()
    return render_template('show_income_entry.html', current_user=current_user, sql=sql)


@mobileapp.route('edit_income_entry', methods=['GET'])
@login_required
def edit_income_entry():
    id = obj.test_input(request.args.get('id'))
    rowedit = Income_Entry.query.get(int(id))
    return jsonify({"group_name": rowedit.group_name, "group_id": rowedit.group_id})


@mobileapp.route('delete_income_entry', methods=['GET', 'POST'])
@login_required
def delete_income_entry():
    id = obj.test_input(request.form.get('id'))
    where = {"income_id": int(id)}
    try:
        deleted_id = Income_Entry.delete_record(**where)
        return jsonify({"resp": deleted_id, "status": "success"})
    except:
        return jsonify({"resp": "error", "message": "ValueError", "status": "failed"})


@mobileapp.route('expense_group', methods=['GET', 'POST'])
@login_required
def expense_group():
    return render_template('expense_group.html')


@mobileapp.route('expense_entry', methods=['GET', 'POST'])
@login_required
def expense_entry():
    return render_template('expense_entry.html')
