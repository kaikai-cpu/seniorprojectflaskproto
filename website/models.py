from . import db
from flask_login import UserMixin #UserMixin class provides the implementation of class properties
from sqlalchemy.sql import func

##store user info in this database schema/model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(150), unique=True)##Makes sure it can't have the same email.
    password = db.Column(db.String(150))
    profession = db.Column(db.String(150))
    inventory = db.relationship('Inventory')#User should have access to the Inventory they added
    
##this is where nursing inventory is stored
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    Description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())#automatically fills up the time now
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))##associate to the user id
