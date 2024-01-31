"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Person, Planets, Vehiculos, Favoritos
#from models import Person
app = Flask(__name__)
app.url_map.strict_slashes = False
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
################ ENDPOINSTS ###########
@app.route('/user', methods=['GET'])
def handle_hello():
    users_query = User.query.all() #estamos haciendo una consulta a la User para que traiga todos
    users_data = list(map(lambda item: item.serialize(), users_query))#procesamos la info consultada y la volvemos un array
    # print(users_query)
    # print(users_data)
    response_body = {
        "msg": "ok",
        "users": users_data
    }
    #get para obtener todas las personas
@app.route('/persons', methods=['GET'])
def get_all_persons():
    persons_query = Person.query.all() #estamos haciendo una consulta a la User para que traiga todos
    persons_data = list(map(lambda item: item.serialize(), persons_query))#procesamos la info consultada y la volvemos un array
    # print(persons_query)
    # print(persons_data)
    response_body = {
        "msg": "ok",
        "persons": persons_data
    }
    return jsonify(response_body), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)