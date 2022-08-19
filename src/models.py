from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Class User(db.Model):
    _tablename_='User'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,)
    email = db.Column(db.String(100), nullable=False, unique=True)
    people = db.relationship('People', secondary="Favorites_people")
    planets = db.relationship('Planets', secondary="Favoreites_planets")
    vehicles = db.relationship('Vehicles', secondary="Favorites_vehicles")


Favorites_People = db.Table('Favorites_people',
    db.Column('people_id', db.Integer, db.Foreignkey('People.id'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

Favorites_vehicles = db.Table('Favorites_vehicles',
    db.Column('vehicles_id', db.Integer, db.Foreignkey('Vehicles.is'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

Favorites_planets = db.Table('Favorites_planets',
    db.Column('planets_id', db.Integer, db.Foreignkey('Planets.id'), primary_key=True),
    db.Column('users_id', db.Integer, db.Foreignkey('User.id'), primary_key=True)
)

def serialize(self):
    return {
        "id": self.id,
        "username": self.username
    }
