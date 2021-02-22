from flask_restful import Resource
from dodolandapp.common.databaseController import getDodoBird, saveToDatabase, checkDodoAlreadyExists
from dodolandapp.common.S3upload import getS3PublicURL
from dodolandapp.common.buildJSON import buildJSON
from dodolandapp.common.generateName import generateName


from flask import jsonify


class metadata(Resource):
    def get(self, gene):
        try:

            # # gene = int(gene)
            # # Check Valid ID
            # if gene > 5000 or gene < 1:
            #     raise Exception("Enter Valid ID")

            # # IF DODO ALREADY EXISTS
            # dodoAlreadyExists = checkDodoAlreadyExists(gene)

            # if dodoAlreadyExists is not None:
            #     print("Already exists")
            #     return jsonify(buildJSON(dodoAlreadyExists))

            # # SET PUBLIC URL AND ENERGY BASED ON GENE
            # if gene >= 1 and gene <= 1000:
            #     publicURL = getS3PublicURL('1.svg')
            #     energy = 900
            # elif gene >= 1001 and gene <= 2000:
            #     publicURL = getS3PublicURL('2.svg')
            #     energy = 1000
            # elif gene >= 2001 and gene <= 3000:
            #     publicURL = getS3PublicURL('3.svg')
            #     energy = 850
            # elif gene >= 3001 and gene <= 4000:
            #     publicURL = getS3PublicURL('4.svg')
            #     energy = 450
            # elif gene >= 4001 and gene <= 5000:
            #     publicURL = getS3PublicURL('5.svg')
            #     energy = 890

            # # SET EXTERNAL URL
            # externalURL = f"https://www.dodolond.com/dodos/{gene}"

            # # GENERATE UNIQUE NAME
            # name = generateName()

            # # SAVE DODO TO DATABASE
            # dodo = saveToDatabase(name, "", gene, publicURL,
            #                       externalURL, "", "", energy, 1, 0)

            # # RETURN DODO
            # return jsonify(buildJSON(dodo))

            return jsonify({
                "name": "upbeat cat",
                "image": "https://s3-ap-south-1.amazonaws.com/dodoland/1.svg",
                "external_url": "https://www.dodolond.com/dodos/1",
                "attributes": [{
                    "display_type": "boost_number",
                    "trait_type": "energy",
                    "value": 740
                }]
            })

        except Exception as e:
            print(e)
            return {"Error": str(e)}
