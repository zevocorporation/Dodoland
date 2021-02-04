from dodolandapp.common.visibleTraits import ParseVisibleTraits
def buildJSON(dodobird):

    traits = ParseVisibleTraits()
    
    extraArgs=[{
                "display_type": "date",
                "trait_type": "birthday",
                "value": dodobird.birthday
            },{
                "display_type": "boost_number",
                "trait_type": "energy",
                "value": dodobird.energy
            },{
                "display_type": "number",
                "trait_type": "generation",
                "value": dodobird.generation
            },{
                "display_type": "number",
                "trait_type": "breeding fee",
                "value": dodobird.breeding_fee
            }]

    attributes=traits["attributes"]+extraArgs


    returnObj = {
        "name": dodobird.name,
        "description": dodobird.description,
        "image": dodobird.image,
        "external_url": dodobird.external_url,
        "background_color": dodobird.background,
        "attributes":attributes
    }

    return returnObj


