from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from vistas import *

from modelos import db



application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://claudia:system$$@aaaf1ndcu93o8p.ckknahbrrseo.us-east-1.rds.amazonaws.com:5432/listanegra'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JWT_SECRET_KEY'] = 'frase-secreta'
application.config['PROPAGATE_EXCEPTIONS'] = True

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()
cors = CORS(application)

api = Api(application)

api.add_resource(VistaSignin, '/auth/signup')
api.add_resource(VistaLogin, '/auth/login')
api.add_resource(VistaBlackList, '/blacklists')
api.add_resource(VistaBlackListDetail, '/blacklists/<string:email>')
api.add_resource(VistaPing, '/')


jwt = JWTManager(application)

if __name__ == "__main__":
    application.run(port = 5000, debug = True)
