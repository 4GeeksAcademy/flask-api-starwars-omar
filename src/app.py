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
from models import db, User , Person, Planets, Vehicles, Favorite_Planet,Favorite_Person,Favorite_Vehicle
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
    return jsonify(response_body), 200
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
    #get para obtener todas los planetas 
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets_query = Planets.query.all() #estamos haciendo una consulta a la User para que traiga todos
    planets_data = list(map(lambda item: item.serialize(), planets_query))#procesamos la info consultada y la volvemos un array
    # print(planets_query)
    # print(planets_data)
    response_body = {
        "msg": "ok",
        "planets": planets_data
    }
    return jsonify(response_body), 200
    #get para obtener todas los vehiculos 
@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles_query = Vehicles.query.all() #estamos haciendo una consulta a la User para que traiga todos
    vehicles_data = list(map(lambda item: item.serialize(), vehicles_query))#procesamos la info consultada y la volvemos un array
    # print(vehicles_query)
    # print(vehicles_data)
    response_body = {
        "msg": "ok",
        "vehicles": vehicles_data
    }
    return jsonify(response_body), 200
    #get para obtener todas los favoritos 
@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    # favorites_query = Favorites.query.all() #estamos haciendo una consulta a la User para que traiga todos
    # favorites_data = list(map(lambda item: item.serialize(), favorites_query))#procesamos la info consultada y la volvemos un array
    # # print(favorites_query)
    # # print(favorites_data)
    # response_body = {
    #     "msg": "ok",
    #     "favorites": favorites_data
    # }
    Favorites_Planets = Favorite_Planet.query.all()
    Favorites_Persons = Favorite_Person.query.all()
    Favorites_Vehicles = Favorite_Vehicle.query.all()
    all_favorite_person = list(map(lambda x : x.serialize(), Favorites_Persons))
    all_favorite_planet = list(map(lambda x : x.serialize(), Favorites_Planets))
    all_favorite_vehicle = list(map(lambda x : x.serialize(), Favorites_Vehicles))
    return jsonify({"planets": all_favorite_planet},{"persons": all_favorite_person},{"vehicles": all_favorite_vehicle}), 200

@app.route('/favorite/person/', methods=['GET'])
def get_favorite_person():
    favoritesPerson = Favorite_Person.query.all()
    all_favorite_Person = list(map(lambda x: x.serialize(), favoritesPerson))
    return jsonify(all_favorite_Person), 200

@app.route('/favorite/planet/', methods=['GET'])
def get_favorite_planet():
    Favorites_Planet = Favorite_Planet.query.all()
    all_favorite_Planet = list(map(lambda x: x.serialize(), Favorites_Planet))
    return jsonify(all_favorite_Planet), 200

@app.route('/favorite/vehicle/', methods=['GET'])
def get_favorite_vehicle():
    FavoritesVehicle = Favorite_Vehicle.query.all()
    all_favorite_vehicle= list(map(lambda x: x.serialize(),  FavoritesVehicle))
    return jsonify(all_favorite_vehicle), 200

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

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    # print(people_id)
    planet_query = Person.query.filter_by(id=planet_id).first()
    # print(people_query.serialize())
 
    response_body = {
        "msg": "ok", 
        "planet": planet_query.serialize()
    }
    return jsonify(response_body), 200
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_one_vehicle(vehicle_id):
    # print(people_id)
    vehicle_query = Person.query.filter_by(id=vehicle_id).first()
    # print(people_query.serialize())
 
    response_body = {
        "msg": "ok", 
        "planet": vehicle_query.serialize()
    }
    return jsonify(response_body), 200

@app.route('/people/<int:people_id>', methods=['POST'])
def create_one_people(people_id):
    # print(people_id)
    people_query = Person.query.filter_by(id=people_id).first()
    # print(people_query.serialize())
 
    response_body = {
        "msg": "ok", 
        "people": people_query.serialize()
    }
    return jsonify(response_body), 200

@app.route('/favorite/person/', methods=['POST'])
def add_favorite_person():
    request_body_Favorite_Person = request.get_json()
    new_favoritePerson = Favorite_Person(user_id=request_body_Favorite_Person["user_id"], person_id=request_body_Favorite_Person["person_id"])
    db.session.add(new_favoritePerson)
    db.session.commit()
    response={"msg": "Its OK"}
    return jsonify(response), 200
                              # hay que hacer dos rutas mas para Vehicles y para planets 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)