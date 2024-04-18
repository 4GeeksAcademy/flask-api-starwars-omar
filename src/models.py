from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }
class Person (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_personaje = db.Column(db.String(100), unique=True)
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    color_ojos =  db.Column(db.String(50))
    color_cabello = db.Column(db.String(50))
    altura = db.Column(db.String(20))
    favorites = db.relationship('Favorites', backref='person', lazy=True)
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
    name = db.Column(db.String(100))
    climate = db.Column(db.String(50))
    terrain= db.Column(db.String(250))
    rotation= db.Column(db.String(250))
    population= db.Column(db.String(250))
    orbital_period= db.Column(db.String(250))
    diameter= db.Column(db.String(250))
    favorites = db.relationship('Favorites', backref='planets', lazy=True)
    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "rotation": self.rotation,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter
            # do not serialize the password, its a security breach
        }
class Vehicles (db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name_Vehicles = db.Column(db.String(50))
    model = db.Column(db.String(50))
    favorites = db.relationship('Favorites', backref='vehicles', lazy=True)
    def __repr__(self):
        return '<Vehicles %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name_Vehicles": self.name_Vehicles,
            "model": self.model
            # do not serialize the password, its a security breach
        }
class Favorites (db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    id_person = db.Column(db.Integer, db.ForeignKey('person.id'))
    def __repr__(self):
        return '<Favorites %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_planets": self.id_planets,
            "id_vehicles": self.id_vehicles,
            "id_person": self.id_person
        }
