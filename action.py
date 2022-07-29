
from config import *


class Actionclass(db.Model):

    __abstract__ = True

    @staticmethod
    def uploadImage(file1, moreFolder=""):
        dt = datetime.now()
        realTime = dt.strftime("%d%m%y%I%M%S%f")
        extn = file1.filename.split(".")[-1]
        imgname = str(realTime)+"."+extn
        if moreFolder != "":
            path = os.path.join(
                app.config['UPLOAD_FOLDER'], moreFolder, imgname)
        else:
            path = os.path.join(app.config['UPLOAD_FOLDER'], imgname)
        file1.save(path)
        return imgname

    @staticmethod
    def removeImage(oldimg, moreFolder=""):
        if oldimg != "":
            if moreFolder != "":
                path = os.path.join(
                    app.config['UPLOAD_FOLDER'], moreFolder, oldimg)
            else:
                path = os.path.join(app.config['UPLOAD_FOLDER'], oldimg)
            os.remove(path)
        return True

    @staticmethod
    def test_input(textContent):
        return escape(textContent.strip())

    @staticmethod
    def dateusa(date_str):
        if date_str != "" and date_str.find("-") > 0:
            datetime_obj = datetime.strptime(date_str, '%d-%m-%Y')
            return datetime_obj.date()
        else:
            return ""

    @staticmethod
    def dateindia(date_str):
        if date_str != "":
            datetime_obj = date_str.strftime("%d-%m-%Y")
            return datetime_obj
        else:
            return ""

    @staticmethod
    def ipaddress():
        return request.remote_addr

    @staticmethod
    def createdate():
        createdate = datetime.now()
        return createdate.date()

    # @classmethod
    # def bulk_save(cls, *args, **kwargs):
    #    qry = cls.query.filter_by(args[0]==args[1]).update({cls.args[0]:'b'})
    #    db.session.commit()
    #    return self

    # def delete(self):
    #    db.session.delete(self)
    #    db.session.commit()
    #    return self

    def adminSession(self):
        if ("userid" in session) and ("usertype" in session):
            return session["userid"]
        else:
            return False

    @classmethod
    def checkLogin(cls, username, password):
        element = cls.query.filter_by(username=username, password=password)
        if(element.count() == 1):
            session["userid"] = element.first().userid
            session["usertype"] = element.first().usertype
            return True
        else:
            return False

    @classmethod
    def insert_record(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        if commit:
            db.session.commit()
        return instance

    @classmethod
    def save_all(cls, requested, tblpkey, commit=False):
        form_data = {}
        for key in requested.form.keys():
            print(key, requested.form.get(key)[0])
            if key != "" and key != None and key != "csrf_token" and key != tblpkey:
                form_data[key] = requested.form.get(key)
        if len(form_data) > 0:
            instance = cls(**form_data)
            db.session.add(instance)
            if commit:
                db.session.commit()
            return instance

    @classmethod
    def delete_record(cls, commit=True, **kwargs):
        instance = cls.query.filter_by(**kwargs).delete()
        if commit:
            db.session.commit()
        return instance

    @classmethod
    def select_record(cls, **kwargs):
        instance = cls.query.filter_by(**kwargs).first()
        return instance

    @classmethod
    def update_record(cls, args, **kwargs):
        # keyvalue = {args[0]: args[1]}
        instance = cls.query.get(args)
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.session.commit()
        return instance

    # @staticmethod
    # def show(post):
    #     data = dict((key, post.form.getlist(key) if len(post.form.getlist(
    #         key)) > 1 else post.form.getlist(key)[0]) for key in post.form.keys())
    #     return data
    @staticmethod
    def show(requested):
        data = {}
        # data = dict((key, requested.form.getlist(key) if len(requested.form.getlist(key)) > 1 else requested.form.getlist(key)[0]) for key in requested.form.keys())
        for key in requested.form.keys():
            print(key, requested.form.get(key)[0])
            if key != "" or key != None:
                data[key] = requested.form.get(key)
        return data


obj = Actionclass()
