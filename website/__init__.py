from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "smarthome.db"


def create_app():
    app = Flask(__name__)
  #  app.config['SECRET_KEY'] = 'jwvxrnycjiuiya'
   # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://iyrnuskvuduxvu:3e08e0a7c29702ee95a8bc36e5b92aaa50cf9ae5e27487639f5cae7635142bfa@ec2-3-224-8-189.compute-1.amazonaws.com:5432/d4b6mr28e6a495'
    app.config['SECRET_KEY'] = 'KEY'


    db.init_app(app)

   
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Room

    # create_database(app)
    #db.create_all(app)

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
