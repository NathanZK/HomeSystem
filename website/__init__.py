from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "smarthome.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KEY'
   # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://jwvxrnycjiuiya:cd58b20126af4c856c34f6613271b0d9fe7b9ff55599d5324228eca792275baa@ec2-34-194-73-236.compute-1.amazonaws.com:5432/d8qu6vjf3b17d4'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Room

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)




    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
