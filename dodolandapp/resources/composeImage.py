from flask_restful import Resource,reqparse
import xml.etree.ElementTree as ET
from flask import jsonify
import random

from dodolandapp.common.changeColors import changeColors
from dodolandapp.common.generateXML import generateXML
from dodolandapp.common.generateName import generateName
from dodolandapp.common.visibleTraits import ParseVisibleTraits,s3Imageupload,getS3PublicURL
from dodolandapp.common.databaseController import saveToDatabase,getMaxID
from dodolandapp.common.buildJSON import buildJSON

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

            # HardCoded traits
            traits = {
                "attributes": [
                    {
                        "trait_type": "tail",
                        "value": "tail1"
                    },
                    {
                        "trait_type": "pattern",
                        "value": "pattern1"
                    },
                    {
                        "trait_type": "head",
                        "value": "head1"
                    },
                    {
                        "trait_type": "hair",
                        "value": "hair1"
                    },
                    {
                        "trait_type": "eyes",
                        "value": "eyes1"
                    },
                    {
                        "trait_type": "Base_color",
                        "value": '#EE6123'
                    },
                    {
                        "trait_type": "Highlight_color",
                        "value": "#F59F7A"
                    },
                    {
                        "trait_type": "Accent_color",
                        "value": "#FFCF00"
                    }
                    
                ]
            }

            # Get colors from traits
            baseColor = traits['attributes'][5]['value']
            highlightColor = traits['attributes'][6]['value']
            accentColor = traits['attributes'][7]['value']


            # Generate XML file
            templateXML = generateXML(traits['attributes'][0:5])

            # Change Image colors
            XMLfile = changeColors(templateXML, baseColor, highlightColor,accentColor)

            # Stringify XML ElementTree Object.. 
            XMLContent = ET.tostring(XMLfile.getroot(), encoding='unicode')

            # Write output
            # XMLfile.write('output1.svg', encoding="us-ascii")

            maxID=getMaxID()
            if maxID is not None:
                maxID=maxID+1
            else:
                maxID=1
            
            background_color=['#BEEACF','#ECC4D9','#EFD4BF','#DDDDDD','#F8C7C1']

            #generate name
            name= generateName()

            # Flag to ensure s3-Image-Uploading-Process.
            IsImageUploaded =  s3Imageupload(XMLContent,maxID)

            # Get public access URL of s3-Object..
            if IsImageUploaded:
                publicURL = getS3PublicURL(f'{maxID}.svg')
                
            else:
                print("Whoops! Something Went Wrong! Flag Status :",IsImageUploaded)
                raise Exception("S3 Image upload error")
            
            # Save dodobird to databse
            dodobird=saveToDatabase(name,"",args.gene,publicURL,"https://www.dodolond/dodos/"+str(maxID),random.choice(background_color),args.birthday,args.energy,args.generation,args.breedingfee)

            returnJSON=buildJSON(dodobird)

            # Return JSON
            return jsonify(returnJSON)

        # Return error msg
        except Exception as e:
            print(e)
            return {"data": "An error occured!"}
