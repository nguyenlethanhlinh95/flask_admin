from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.secret_key = 'Thisissecrectkey'
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)  # SQL Achemy
admin = Admin(app, template_mode='bootstrap3')


# silly user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    join_date = db.Column(db.DateTime)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class UserView(ModelView):
    column_exclude_list = ['join_date']
    # column_filters = ['name', 'email']
    can_export = False
    column_display_pk = True
    can_create = True
    can_delete = True
    can_edit = True

    # def on_model_change(self, form, model, is_created):
    #     model.password = generate_password_hash(model.password, method='sha256')


@app.route('/')
def hello_world():
    return 'Hello World!'


admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(Test, db.session))

if __name__ == '__main__':
    app.run()
