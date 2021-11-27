from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'fl@sk_sen1or.pr0j3ct'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    
    #user who isnt authenticated is redirected to the login page
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    
   

    ##import blueprints from auth.py and main.py
    ##auth blueprint for login, sign-out
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    ##main blueprint for index and profiles
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    ##inventory blueprint for inventories
    from .inventory import inventory as inventory_blueprint
    app.register_blueprint(inventory_blueprint)
    
    from .models import User, Inventory ##imports the database model for invenotry and user
    create_database(app)

     #User loader finds user with active session and creates cookies. User Id is stored in that cookie.
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

def create_database(app):
    if not path.exists('SENIORPROJECTFLASKPROTO/' + DB_NAME):##checks database if it exists
        db.create_all(app=app)
        print('Created Database')

