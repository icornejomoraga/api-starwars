import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Planets, Character, Vehicles, Starships
from flask_migrate import Migrate
#from flask_script import Manager

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
#manager = Manager(app)

db.init_app(app)
Migrate(app, db)

@app.route('/')
def home():
    return jsonify('Hola Mundo')

@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "GET":
        user = User.query.get(1)
        if user is not None:
            return jsonify(user.serialize_just_username())
    else:
        user = User()
        user.name = request.json.get("name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        user.isActive = request.json.get("isActive")
        
        
        db.session.add(user)
        db.session.commit()
    
    return jsonify(user.serialize()), 200


@app.route("/planets", methods=["POST", "GET"])
def planets(): 
    if request.method == "GET":
        planets = Planets.query.get(1)
        if planets is not None:
            return jsonify(planets.serialize_just_planetname())   
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.rotation_period = request.json.get("rotation_period")
        planets.climate = request.json.get("climate")
        planets.terrain = request.json.get("terrain")
        planets.population = request.json.get("population")
        
            
        db.session.add(planets)
        db.session.commit()
    
    return jsonify(planets.serialize()), 200



@app.route("/character", methods=["POST", "GET"])
def character():    
    if request.method == "GET":
        character = Character.query.get(1)
        if character is not None:
            return jsonify(character.serialize_just_charactername())   
    else:
    
        character = Character()
        character.name = request.json.get("name")
        character.gender = request.json.get("gender")
        character.height = request.json.get("height")
        character.hair_color = request.json.get("hair_color")
        character.skin_color = request.json.get("skin_color")
        character.birth_year = request.json.get("birth_year")
        
        
        db.session.add(character)
        db.session.commit()
    
        return jsonify(character.serialize()), 200


@app.route("/vehicles", methods=["POST", "GET"])
def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serialize_just_vehiclesname())  
        
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get('name')
        vehicles.model = request.json.get('model')
        vehicles.passengers = request.json.get('passengers')
        vehicles.manufacturer = request.json.get('manufacturer')
        vehicles.cost_in_credits = request.json.get('cost_in_credits')     
        
        db.session.add(vehicles)
        db.session.commit()

        return jsonify(vehicles.serialize()), 200


@app.route("/starships", methods=["POST", "GET"])
def starships(): 
    if request.method == "GET":
        starships = Starships.query.get(1)
        if starships is not None:
            return jsonify(starships.serialize_just_Starshipsname())   
    else:
        starships = Starships()
        starships.name = request.json.get("name")
        starships.model = request.json.get("model")
        starships.cargo_capacity = request.json.get("cargo_capacity")
        starships.passengers = request.json.get("passengers")
        starships.max_atmosphering_speed = request.json.get("max_atmosphering_speed")
                
            
        db.session.add(starships)
        db.session.commit()
    
        return jsonify(starships.serialize()), 200




if __name__ == "__main__":
    app.run(host='localhost', port=8080)    