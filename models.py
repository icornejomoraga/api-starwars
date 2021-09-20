from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    isActive = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'password':self.password,
            'email':self.email,
            'isActive':self.isActive,
        }
    
    def serialize_just_username(self):
        return {
            'id':self.id,
            'name':self.name
        }


        

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    rotation_period = db.Column(db.String(10))
    climate = db.Column(db.String(30), nullable=False)
    terrain = db.Column(db.String(30), default=False)
    population = db.Column(db.String(30), default=False)
    
    

    def __repr__(self):
        return "<Planets %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'rotation_period':self.rotation_period,
            'climate':self.climate,
            'terrain':self.terrain,
            'population':self.population,
        }
    def serialize_just_planetname(self):
        return {
            'id':self.id,
            'name':self.name
        }



class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.String(10))
    hair_color = db.Column(db.String(30))
    skin_color = db.Column(db.String(30))
    birth_year = db.Column(db.String(30), default=False)
    


    def __repr__(self):
        return "<Character %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'gender':self.gender,
            'height':self.height,
            'hair_color':self.hair_color,
            'skin_color':self.skin_color,
            'birth_year':self.birth_year,
            }
     
    def serialize_just_charactername(self):
        return {
            'id':self.id,
            'name':self.name
            }
   

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    passengers = db.Column(db.String(30))
    manufacturer = db.Column(db.String(30))
    cost_in_credits = db.Column(db.String(30), nullable=False)
    
    
    

    def __repr__(self):
        return "<vehicles %r>" % self.id

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'passengers': self.passengers,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
        }
        
    def serialize_just_vehiclesname(self):
        return {
            'id':self.id,
            'name':self.name
        }
   


class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    cargo_capacity = db.Column(db.String(30), nullable=False)
    passengers = db.Column(db.String(30), default=False)
    max_atmosphering_speed = db.Column(db.String(30))
    
    

    def __repr__(self):
        return "<Starships %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'model':self.model,
            'cargo_capacity':self.cargo_capacity,
            'passengers':self.passengers,
            'max_atmosphering_speed':self.max_atmosphering_speed,
        }
    def serialize_just_Starshipsname(self):
        return {
            'id':self.id,
            'name':self.name
        }

class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
  

    def __repr__(self):
        return "<Favoritos %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            
        }
    
   