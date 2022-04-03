from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from vistas import *

from modelos import db


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///black_list.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)

api.add_resource(VistaSignin, '/auth/signup')
api.add_resource(VistaLogin, '/auth/login')
api.add_resource(VistaBlackList, '/blacklists')
api.add_resource(VistaBlackListDetail, '/blacklists/<string:email>')
api.add_resource(VistaPing, '/ping')


jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3020)
