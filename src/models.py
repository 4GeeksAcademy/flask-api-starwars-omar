from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "nombre":self.nombre,
            "email": self.email
            # do not serialize the password, its a security breach
        }
class Person (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_personaje = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    color_ojos =  db.Column(db.String(50), nullable=False)
    color_cabello = db.Column(db.String(50), nullable=False)
    altura = db.Column(db.String(20), nullable=False)
    favorites = db.relationship('Favorites_Person', backref='person', lazy=True)
    def __repr__(self):
        return '<Person  %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje,
            "edad": self.edad,
            "genero": self.genero,
            "color_ojos": self.color_ojos,
            "color_cabello": self.color_cabello,
            "altura": self.altura
        }
class Planets (db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    clima = db.Column(db.String(50),nullable=False)
    terreno= db.Column(db.String(250),nullable=False)
    rotación= db.Column(db.String(250),nullable=False)
    población= db.Column(db.String(250),nullable=False)
    periodo_orbital= db.Column(db.String(250),nullable=False)
    diametro= db.Column(db.String(250),nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)
    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.climate,
            "terreno": self.terrain,
            "rotacion": self.rotation,
            "poblacion": self.population,
            "periodo_orbital": self.orbital_Period,
            "diametro": self.diameter
            # do not serialize the password, its a security breach
        }
class Vehicles (db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name_Vehicles = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    favorites = db.relationship('Favorites', backref='vehicles', lazy=True)
    def __repr__(self):
        return '<vehicles %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name_Vehicles": self.name_Vehicles,
            "model": self.model
            # do not serialize the password, its a security breach
        }
# class Favorites (db.Model):
#     __tablename__ = 'favorites'
#     id = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
#     id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
#     id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
#     id_person = db.Column(db.Integer, db.ForeignKey('person.id'))
#     def __repr__(self):
#         return '<Favorites %r>' % self.id
#     def serialize(self):
#         return {
#             "id": self.id,
#             "id_user": self.id_user,
#             # do not serialize the password, its a security breach
#         }
class Favorite_Person(db.model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    id_person = db.Column(db.Integer, db.ForeignKey('Person.id'))
    def __repr__(self):
        return '<FavoritesPerson %r>' % self.id
    def serialize(self):
        return {
             "id": self.id,
             "id_user": self.id_user,
             "id_person": self.id_person
        }
class Favorite_Planet(db.model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    id_planet = db.Column(db.Integer, db.ForeignKey('Planet.id'))
    def __repr__(self):
        return '<FavoritesPlanet %r>' % self.id
    def serialize(self):
        return {
             "id": self.id,
             "id_user": self.id_user,
             "id_planet": self.id_planet
        }

class Favorite_Vehicle(db.model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    id_vehicle = db.Column(db.Integer, db.ForeignKey('Vehicle.id'))
    def __repr__(self):
        return '<FavoritesVehicle %r>' % self.id
    def serialize(self):
        return {
             "id": self.id,
             "id_user": self.id_user,
             "id_Vehicle": self.id_vehicle
        }