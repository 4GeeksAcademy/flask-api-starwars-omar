from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', backref='user', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
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
    favoritos = db.relationship('Favoritos', backref='person', lazy=True)
    def __repr__(self):
        return '<Person  %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "nombre_personaje": self.nombre_personaje,
            "edad": self.edad,
            "genero": self.Genero,
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
    favoritos = db.relationship('Favoritos', backref='planets', lazy=True)
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
class Vehiculos (db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name_Vehicles = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    favoritos = db.relationship('Favoritos', backref='vehiculos', lazy=True)
    def __repr__(self):
        return '<Vehiculos %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "name_Vehicles": self.name_Vehicles,
            "model": self.model
            # do not serialize the password, its a security breach
        }
class Favoritos (db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    id_vehiculos = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    id_person = db.Column(db.Integer, db.ForeignKey('person.id'))
    def __repr__(self):
        return '<Favoritos %r>' % self.id
    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            # do not serialize the password, its a security breach
        }