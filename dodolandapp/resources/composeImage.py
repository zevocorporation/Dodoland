from flask_restful import Resource
import xml.etree.ElementTree as ET
from flask import jsonify

from dodolandapp.common.changeColors import changeColors
from dodolandapp.common.generateXML import generateXML
from dodolandapp.common.generateName import generateName
from dodolandapp.common.visibleTraits import ParseVisibleTraits,s3Imageupload,getS3PublicURL
from dodolandapp.common.saveToDatabase import saveToDatabase

# Class Handling Image Composition


class ComposeImage(Resource):
    def get(self):
        try:

            # Call Decode traits
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


            baseColor = traits['attributes'][5]['value']
            highlightColor = traits['attributes'][6]['value']
            accentColor = traits['attributes'][7]['value']


            # Generate XML file
            templateXML = generateXML(traits['attributes'][0:5])

            # Change Image colors
            XMLfile = changeColors(templateXML, baseColor, highlightColor,accentColor)

            

            # Write output
            XMLfile.write('output1.svg', encoding="us-ascii")
           
            # Stringify XML ElementTree Object.. 
            XMLContent = ET.tostring(XMLfile.getroot(), encoding='unicode')
            
            # Flag to ensure s3-Image-Uploading-Process.
            IsImageUploaded =  s3Imageupload(XMLContent)
            
            
            # Get public access URL of s3-Object..
            if IsImageUploaded:
                publicURL = getS3PublicURL()
                print(publicURL)
            else:
                print("Whoops! Something Went Wrong! Flag Status :",IsImageUploaded)
            
                
            name= generateName()
            print(name)
            # Return JSON
            return jsonify(ParseVisibleTraits())

        # Return error msg
        except Exception as e:
            print(e)
            return {"data": "An error occured!"}
