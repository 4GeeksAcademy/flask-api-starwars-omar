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
from models import db, User , Person, Planets, Vehicles, Favorites
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

#from models import Person
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

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
    return jsonify(response_body), 200
    #get para obtener todas las personas
# METODO GET PARA PERSON
@app.route('/persons', methods=['GET'])
def get_all_persons():
    persons_query = Person.query.all() #estamos haciendo una consulta a la persons para que traiga todos
    persons_data = list(map(lambda item: item.serialize(), persons_query))#procesamos la info consultada y la volvemos un array
    # print(persons_query)
    # print(persons_data)
    response_body = {
        "msg": "ok",
        "persons": persons_data
    }
    return jsonify(response_body), 200
# METODO GET PARA PLANETAS
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets_query = Planets.query.all()
    planets_data = list(map(lambda item: item.serialize(), planets_query))
    response_body = {
        "msg": "ok",
        "planets": planets_data
}
    return jsonify(response_body), 200
# medoto GET para vehiculos
@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles_query = Vehicles.query.all()
    vehicles_data = list(map(lambda item: item.serialize(), vehicles_query))
    response_body = {
        "msg": "ok",
        "vehicles": vehicles_data
}
    return jsonify(response_body), 200
#metodo GET para favoritos
@app.route('/favorites', methods=['GET'])
@jwt_required()
def get_all_favorites():
    current_user = get_jwt_identity()
    # favorites_query = Favorites.query.all()
    # favorites_data = list(map(lambda item: item.serialize(), favorites_query))
    user_favorites_query = User.query.filter_by(email = current_user)
    user_favorites_data = list(map(lambda item: item.serialize(), user_favorites_query))

    print(user_favorites_data)
    response_body = {
        "msg": "ok",
        "data":user_favorites_data
    
}
    return jsonify(response_body), 200
#para obtener datos de UNA sola PERSONA
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    # print(people_id)
    people_query = Person.query.filter_by(id=people_id).first()
    # print(people_query.serialize())
    response_body = {
        "msg": "ok",
        "people": people_query.serialize()
    }
    return jsonify(response_body), 200
#para obtener datos de UN sola VEHICULO
@app.route('/vehicle/<int:vehicles_id>', methods=['GET'])
def get_one_vehicle(vehicle_id):
    # print(vehicles_id)
    vehicle_query = Person.query.filter_by(id=vehicle_id).first()
    # print(people_query.serialize())
    response_body = {
        "msg": "ok",
        "vehicles": vehicle_query.serialize()
    }
    return jsonify(response_body), 200
#para obtener datos de UN solo PLANETA
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    # print(vehicles_id)
    planet_query = Person.query.filter_by(id=planet_id).first()
    # print(people_query.serialize())
    response_body = {
        "msg": "ok",
        "planets": planet_query.serialize()
    }
    return jsonify(response_body), 200
# POST para CREAR una nueva persona
@app.route('/people', methods=['POST'])
def create_one_people():
    body = request.json
    new_people = Person(name=body["name"])
    db.session.add(new_people)
    db.session.commit()
    response_body = {
        "msg": "person created",
        # "people": people_query.serialize
    }
    return jsonify(response_body), 200
# POST para CREAR un nuevo PLANETA
@app.route('/planets', methods=['POST'])
def create_one_planet():
    body = request.json
    # print(body)
    new_planet = Planets(name=body["name"], climate=body["climate"], terrain=body["terrain"], rotation=body["rotation"], population=body["population"], orbital_period=body["orbital_period"], diameter=body["diameter"])
    # print(new_planet)
    db.session.add(new_planet)
    db.session.commit()
    response_body = {
        "msg": "planet created",
        # "people": people_query.serialize
    }
    return jsonify(response_body), 200
       


@app.route("/login", methods=["POST"])
def login():
    # body = request.json
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user_query = User.query.filter_by(email=email).first()

    print(user_query.email)

    if email != user_query.email or password != user_query.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)