from dodolandapp.models import CreatedBirds
from dodolandapp import db
from sqlalchemy import func


# SAVE DODO TO DATABSE
def saveToDatabase(name, description, gene, image, external_url, background, birthday, energy, generation, breeding_fee):
    try:
        createdBird = CreatedBirds(name=name, description=description, gene=gene, image=image, external_url=external_url,
                                   background=background, birthday=birthday, energy=energy, generation=generation, breeding_fee=breeding_fee)
        db.session.add(createdBird)
        db.session.commit()
        return createdBird

    except Exception as e:
        raise e


# CHECK IF DODO ALREADY EXISTS BY GENE
def checkDodoAlreadyExists(gene):
    try:
        dodobird = CreatedBirds.query.filter(CreatedBirds.gene == gene).first()
        return dodobird
    except Exception as e:
        raise e


# CHECK IF DODO ALEADY EXISTS BY ID
def getDodoBird(id):
    try:
        dodobird = CreatedBirds.query.filter(CreatedBirds.id == id).first()
        return dodobird
    except Exception as e:
        raise e
