import random
from dodolandapp.models import CreatedBirds

def generateName():
    try:
        nounsFile = "dodolandapp/assets/words/nouns.txt"
        verbsFile = "dodolandapp/assets/words/verbs.txt"
        nouns = open(nounsFile).read().splitlines()
        verbs = open(verbsFile).read().splitlines()
        name=""
        nameFound=True
        while nameFound:
            name = random.choice(verbs)+" "+random.choice(nouns)
            if not bool(CreatedBirds.query.filter_by(name=name).first()):
                nameFound=False
        return name
    except Exception as e:
        raise e
