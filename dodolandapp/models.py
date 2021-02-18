from dodolandapp.db import db


class CreatedBirds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500))
    gene = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(500), nullable=False)
    external_url = db.Column(db.String(500), unique=True, nullable=False)
    background = db.Column(db.String(7), nullable=False)
    birthday = db.Column(db.BigInteger, nullable=False)
    energy = db.Column(db.BigInteger, nullable=False)
    generation = db.Column(db.Integer, nullable=False)
    breeding_fee = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"DodoBird('{self.id}','{self.gene}','{self.image}','{self.external_url}','{self.background}','{self.birthday}','{self.energy}','{self.generation}','{self.breeding_fee}')"
