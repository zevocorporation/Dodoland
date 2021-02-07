from flask_restful import Resource
from dodolandapp.common.databaseController import getDodoBird
from dodolandapp.common.buildJSON import buildJSON
from flask import jsonify


class metadata(Resource):
    def get(self, id):
        try:
            dodobird = getDodoBird(id)
            if dodobird is None :
                raise Exception("Enter valid ID")
            
            jsonObj = buildJSON(dodobird)

            return jsonify(jsonObj)

        except Exception as e:
            print(e)
            return {"Error": str(e)}
