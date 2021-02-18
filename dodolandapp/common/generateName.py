import random
from dodolandapp.models import CreatedBirds

# GENERATE UNIQUE NAME


def generateName():
    try:
        # READ WORDS
        nounsFile = "dodolandapp/assets/words/nouns.txt"
        verbsFile = "dodolandapp/assets/words/verbs.txt"

        # CREATE WORD ARRAY
        nouns = open(nounsFile).read().splitlines()
        verbs = open(verbsFile).read().splitlines()

        # LOOP TILL UNIQUE NAME GENERATED
        nameFound = True
        while nameFound:
            name = random.choice(verbs)+" "+random.choice(nouns)
            if not bool(CreatedBirds.query.filter_by(name=name).first()):
                nameFound = False

        # RETURN UNIQUE NAME
        return name
    except Exception as e:
        raise e
