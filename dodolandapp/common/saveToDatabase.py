from dodolandapp.models import CreatedBirds
from dodolandapp import db


def saveToDatabase(name,description,gene,image,external_url,background,birthday,energy,generation,breeding_fee):
    try:
        createdBird= CreatedBirds(name=name,description=description,gene=gene,image=image,external_url=external_url,background=background,birthday=birthday,energy=energy,generation=generation,breeding_fee=breeding_fee)
        db.session.add(createdBird)
        db.session.commit()

    except Exception as e:
        raise e
        