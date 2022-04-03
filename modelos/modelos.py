import enum

from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
class GlobalList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_uuid = db.Column(db.String(50))
    email = db.Column(db.String(50))
    blocked_reason = db.Column(db.String(50))
    ip = db.Column(db.String(50))
    date = db.Column(db.DateTime)

class GlobalListSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GlobalList
        include_relationships = True
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


