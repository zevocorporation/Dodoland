# BUILD JSON OBJECT TO BE RETURNED
def buildJSON(dodobird):
    returnObj = {
        "name": dodobird.name,
        "image": dodobird.image,
        "external_url": dodobird.external_url,
        "energy": dodobird.energy
    }

    return returnObj
