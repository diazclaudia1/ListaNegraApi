from modelos import db, GlobalList, GlobalListSchema, User, UserSchema
from flask import current_app, request, send_file
import socket
from utils import *
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import requests
import os
import uuid
import time
import json
import io
from datetime import datetime

# Current date time in local system
print()

globalList_schema = GlobalListSchema()
user_schema = UserSchema()


class VistaSignin(Resource):

    def post(self):
        if request.json["password1"] != request.json["password2"]:
            return "Password do not match", 400
        else:
            new_user = User(
                username=request.json["username"], password=request.json["password1"])
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity=new_user.id)
            return {"message": "User created successfully", "token": access_token}


class VistaLogin(Resource):

    def post(self):
        user = User.query.filter(
            User.username == request.json["username"], User.password == request.json["password"]).first()
        db.session.commit()
        if user is None:
            return "User not exit", 404
        else:
            access_token = create_access_token(identity=user.id)
            return {"message": "Successful login", "token": access_token}


class VistaBlackList(Resource):

    @jwt_required()
    def post(self):
        identity = get_jwt_identity()
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)  
        var_uuid=uuid.uuid1()     
        add_email = GlobalList(app_uuid=str(var_uuid), email=request.json["email"], blocked_reason=request.json["blocked_reason"], ip=IPAddr, date=datetime.now())
        db.session.add(add_email)
        db.session.commit()
        return globalList_schema.dump(add_email)


class VistaBlackListDetail(Resource):

    @jwt_required()
    def get(self, email):
        identity = get_jwt_identity()
        query_string = "select * from global_list t where t.email =" + \
                       '\'' + str(email) + '\''
        result = db.engine.execute(query_string)
        rta = [dict(row) for row in result]
        if len(rta) == 0:
            return "El email no está en la lista negra", 200
        else:
            return "El email sí está en la lista negra", 200


class VistaPing(Resource):
    def get(self):
        return 'pong', 200
