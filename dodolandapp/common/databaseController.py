from dodolandapp.models import CreatedBirds
from dodolandapp import db
from sqlalchemy import func


def saveToDatabase(name,description,gene,image,external_url,background,birthday,energy,generation,breeding_fee):
    try:
        createdBird= CreatedBirds(name=name,description=description,gene=gene,image=image,external_url=external_url,background=background,birthday=birthday,energy=energy,generation=generation,breeding_fee=breeding_fee)
        db.session.add(createdBird)
        db.session.commit()
        return createdBird;

    except Exception as e:
        raise e

def generateID():
    try:
        query=CreatedBirds.query.with_entities(func.max(CreatedBirds.id).label("maxID")).first()
        if query.maxID is None:
            return 1
        else:
            return query.maxID+1
    except Exception as e:
        raise e

def checkDodoAlreadyExists(gene):
    try:
        dodobird=CreatedBirds.query.filter(CreatedBirds.gene==gene).first()
        return dodobird
    except Exception as e:
        raise e

def getDodoBird(id):
    try:
        dodobird=CreatedBirds.query.filter(CreatedBirds.id==id).first()
        return dodobird
    except Exception as e:
        raise e

        