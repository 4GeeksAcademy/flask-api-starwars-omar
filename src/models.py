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
            "email": self.email,
            "favorites": self.favorites
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
    name = db.Column(db.String(100),nullable=False)
    climate = db.Column(db.String(50),nullable=False)
    terrain= db.Column(db.String(250),nullable=False)
    rotation= db.Column(db.String(250),nullable=False)
    population= db.Column(db.String(250),nullable=False)
    orbital_period= db.Column(db.String(250),nullable=False)
    diameter= db.Column(db.String(250),nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)
    def __repr__(self):
        return '<Planets %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "clima": self.climate,
            "terreno": self.terrain,
            "rotacion": self.rotation,
            "poblacion": self.population,
            "periodo_orbital": self.orbital_period,
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
            # do not serialize the password, its a security breach
        }
class Login (db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    id_email = db.Column(db.Integer, db.ForeignKey('email.id'))
    id_password = db.Column(db.Integer, db.ForeignKey('password.id'))
    def __repr__(self):
        return '<login %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "id_email": self.id_email,
            "id_password":self.id_password

        }