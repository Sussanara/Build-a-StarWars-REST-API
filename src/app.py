from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
Migrate(app, db) # db init, db migrate, db upgrade



if __name__ == '__main__':
        app.run()