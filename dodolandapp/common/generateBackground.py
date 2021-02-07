import random
def generateBackground():
    try:
        background_color=['#BEEACF','#ECC4D9','#EFD4BF','#DDDDDD','#F8C7C1']
        return random.choice(background_color)
    except Exception as e:
        raise e