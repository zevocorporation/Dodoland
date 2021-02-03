from dodolandapp.db import db

# creating Traits model
class Traits(db.Model):
    kaiValue =  db.Column(db.Integer,primary_key = True)
    Head = db.Column(db.String(100),unique = True,nullable = False)
    Beak =  db.Column(db.String(100),unique = True,nullable = False)
    Hair =  db.Column(db.String(100),unique = True,nullable = False)
    Chest =  db.Column(db.String(100),unique = True,nullable = False)
    Body =  db.Column(db.String(100),unique = True,nullable = False)
    Tail =  db.Column(db.String(100),unique = True,nullable = False)
    Talons =  db.Column(db.String(100),unique = True,nullable = False)
    Eyes =  db.Column(db.String(100),unique = True,nullable = False)
    Wings =  db.Column(db.String(100),unique = True,nullable = False)
    Future_1 =  db.Column(db.String(100),unique = True,nullable = False)
    Future_2 =  db.Column(db.String(100),unique = True,nullable = False)
    Future_3 =  db.Column(db.String(100),unique = True,nullable = False)

    def __repr__(self):
        return f"Traits('{self.Head}','{self.Beak}','{self.Hair}','{self.Chest}','{self.Body}','{self.Tail}','{self.Talons}','{self.Eyes}','{self.Wings}','{self.Future_1}','{self.Future_2}','{self.Future_3}')"


class CreatedBirds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100),unique = True,nullable = False)
    description=db.Column(db.String(500),unique = True)
    gene = db.Column(db.String(100),unique = True,nullable = False)
    image= db.Column(db.String(500),unique = True,nullable = False)
    external_url= db.Column(db.String(500),unique = True,nullable = False)
    background= db.Column(db.String(7),unique = True,nullable = False)
    birthday= db.Column(db.String(500),unique = True,nullable = False)
    energy= db.Column(db.BigInteger,unique = True,nullable = False)
    generation= db.Column(db.Integer,unique = True,nullable = False)
    breeding_fee= db.Column(db.Integer,unique = True,nullable = False)
    
    def __repr__(self):
        return f"DodoBird('{self.id}','{self.gene}','{self.image}','{self.external_url}','{self.background}','{self.birthday}','{self.energy}','{self.generation}','{self.breeding_fee}')"
    
    
