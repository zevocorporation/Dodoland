import xml.etree.ElementTree as ET
import re

def generateXML(traits):
    # Register default namespace for XML tags
    ET.register_namespace('', "http://www.w3.org/2000/svg")

    # Create template for XML string
    templateString = '''<svg width="1080" height="1080" viewBox="0 0 1080 1080" fill="none">
                                <g clip-path="url(#clip0)">
                                </g>
                                <defs>
                                <clipPath id="clip0">
                                <rect width="1080" height="1080" fill="white"/>
                                </clipPath>
                                </defs>
                                </svg>'''.strip()

    # Remove spaces in template string
    templateString = re.sub('(\\s+|\\n)', ' ', templateString)

    # Read template string as XML ElementTree element
    template = ET.ElementTree(ET.fromstring(templateString))

    # Get element required to append dodobird parts
    templateRoot = template.getroot()[0]
    

    # For each part append XML code into template XML document
    for part in traits:
        try:
            imagePath = 'dodolandapp/assets/images/{}/{}.svg'.format(part['trait_type'], part['value'])
            tree = ET.parse(imagePath)
            root = tree.getroot()[0]
            for element in root:
                templateRoot.append(element)
        except Exception as e:
            raise e


    return template
