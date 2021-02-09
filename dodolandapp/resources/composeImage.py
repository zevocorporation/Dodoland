from flask_restful import Resource,reqparse
import xml.etree.ElementTree as ET
from flask import jsonify
import random

from dodolandapp.common.changeColors import changeColors
from dodolandapp.common.generateXML import generateXML
from dodolandapp.common.generateName import generateName
from dodolandapp.common.visibleTraits import ParseVisibleTraits,s3Imageupload,getS3PublicURL
from dodolandapp.common.databaseController import saveToDatabase,generateID,checkDodoAlreadyExists
from dodolandapp.common.buildJSON import buildJSON
from dodolandapp.common.generateBackground import generateBackground

# Args parser for Compose Image
composeImageArgs= reqparse.RequestParser();
composeImageArgs.add_argument('gene',type=str,help="genome of dodobird",required=True)
composeImageArgs.add_argument('birthday',type=int,help="genome of dodobird",required=True)
composeImageArgs.add_argument('energy',type=int,help="genome of dodobird",required=True)
composeImageArgs.add_argument('generation',type=int,help="genome of dodobird",required=True)
composeImageArgs.add_argument('breedingfee',type=int,help="genome of dodobird",required=True)

# Class handling compose image
class ComposeImage(Resource):
    def put(self):
        try:
            
            # Parse Args
            args=composeImageArgs.parse_args()

            # Check if dodobird is already created
            dodoAlreadyExists = checkDodoAlreadyExists(args.gene)

            if dodoAlreadyExists is not None:
                print("Already exists")
                return jsonify (buildJSON(dodoAlreadyExists))

            # HardCoded traits
            traits=ParseVisibleTraits()

            # Get colors from traits
            baseColor,highlightColor,accentColor = traits['attributes'][5]['value'],traits['attributes'][6]['value'],traits['attributes'][7]['value']

            # Generate XML file
            templateXML = generateXML(traits['attributes'][0:5])

            # Change Image colors
            XMLfile = changeColors(templateXML, baseColor, highlightColor,accentColor)

            # Stringify XML ElementTree Object.. 
            XMLContent = ET.tostring(XMLfile.getroot(), encoding='unicode')

            #Generate ID 
            dodobirdID=generateID()

            #Generate Name
            dodobirdName= generateName()

            #Generate background
            background_color=generateBackground()

            # Upload SVG to S3
            s3Imageupload(XMLContent,dodobirdID)

            # Get public access URL of s3-Object..
            publicURL = getS3PublicURL(f'{dodobirdID}.svg')
           
            # Save dodobird to databse
            dodobird=saveToDatabase(dodobirdName,"",args.gene,publicURL,"https://www.dodolond.com/dodos/"+str(dodobirdID),background_color,args.birthday,args.energy,args.generation,args.breedingfee)
            
            #Building dodobird additional traits
            dodobirdInfo=buildJSON(dodobird)

            # Return JSON
            return jsonify(dodobirdInfo)

        # Return error msg
        except Exception as e:
            print(e)
            return {"Error": str(e)}
