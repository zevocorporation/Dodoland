import os,logging
import boto3
from dotenv import load_dotenv
from dodolandapp.models import Traits

# env variable configuration..
load_dotenv()

# AWS CREDENTIALS...
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
access_region = os.getenv("access_region")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("bucket_name")

# initaslised traits to be parsed dictionary object..
traitsParsed={
            "attributes": 
                [
                        {
                        "trait_type": "head",
                        "value": "black"
                        },
                        {
                        "trait_type": "beak",
                        "value": ""
                        },
                        {
                        "trait_type": "hair",
                        "value": ""
                        },
                        {
                        "trait_type": "chest",
                        "value": ""
                        },
                        {
                        "trait_type": "body",
                        "value": ""
                        },
                        {
                        "trait_type": "tail",
                        "value": ""
                        },
                        {
                        "trait_type": "talons",
                        "value": ""
                        },
                        {
                        "trait_type": "eyes",
                        "value": ""
                        },
                        {
                        "trait_type": "wings",
                        "value": ""
                        },
                        {
                        "trait_type": "Accent_color",
                        "value": ""
                        },
                        {
                        "trait_type": "Base_color",
                        "value": ""
                        },
                        {
                        "trait_type": "Accent_color",
                        "value": ""
                        },
                ]
}


# 1.enocded gene will be fetched by sending a request to the blockchain API..
# 2. Decoding genes are composed of following three methods..

# 2.1 Fetching Visible Traits..

def getVisibleTraits():
    try:
        
        # print("enter gene")
        gene = 2732197523310061095537000898109269850642884645637264955081144695258221633 
        #encoded gene will replace at runtime.
        express = [None] * 12
        i = 0
        while i < 12:
            express[i] = get5bits(gene , i *4)
            i+=1
        else:
            # print(express) 
            return express
    except Exception as e :
        raise e
    
# 2.2 Kai Represntation..

def get5bits(gene,slot):
    try:
        return int(slicenumber(gene, 5, slot*5))
    except Exception as e:
        raise e
    
    
# 2.3 Bit Masking..

def slicenumber(n,nbits,offset):
   try:
        mask = int((2**nbits) - 1) << offset
        res = (n & mask) >> offset
        return res
   except Exception as e:
       raise e
    

# 3. Pasring the Visible Traits based on requirements..

# 3.1 Parsing the Visible Traits To Compose Image..
def ParseVisibleTraits():
    try:
        traits = getVisibleTraits()  # Refer =>  2.1 -2.3
        for i in range(0,len(traits)):
            dodoBird = Traits.query.filter_by(kaiValue = traits[i]).first()
            traitsParsed["attributes"][i]["value"] = selectTraits(i,dodoBird)   
        return traitsParsed
    except Exception as e:
        raise e
    
# 3.2 Mapping the traits based on requirements:-
def selectTraits(i,dodobird):
    try:
        # mapping the pairs based on DB Traits..
        mappedTraits = {
            0 : dodobird.Head,
            1 : dodobird.Beak,
            2 : dodobird.Hair,
            3 :dodobird.Chest,
            4 : dodobird.Body,
            5 : dodobird.Tail,
            6 : dodobird.Talons,
            7 : dodobird.Eyes,
            8 : dodobird.Wings,
            9 : "Accent_Color",
            10 : "Highlight_Color",
            11 : "Base_color"
        }
        return mappedTraits.get(i,"null")
    
    except Exception as e:
        raise e

#  4. Finally upload the Composed Image to s3..

# 4.1 Upload Composed Image To s3:

def s3Imageupload(XMLcontent,filename):
    try:
            # Setting up s3 instance... 
            s3 = boto3.resource(
            's3',
            region_name = access_region,
            aws_access_key_id = access_key_id,
            aws_secret_access_key = secret_access_key
        )
            # Uploading xml content to s3 Bucket... 
            res = s3.Object(bucket_name,f'{filename}.svg').put(Body=XMLcontent,ACL = 'public-read',ContentType = 'image/svg+xml')
            
            # Note :- Object_name must be replaced with Key_name
            if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return True
            return False
    except Exception as e:
        raise e

# 4.2 Retrive the public URL of the s3 Object..

def getS3PublicURL(filename):
    try:
        # setting up s3 credentials object.. 
        s3Client = boto3.client('s3',aws_access_key_id = access_key_id,
                                    aws_secret_access_key = secret_access_key)
        
    #    fetching s3 Bucket location... 
        bucket_location = s3Client.get_bucket_location(Bucket=bucket_name)

    #   creating Public URL to access it..   
        public_object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        bucket_name,
        filename) 

        return public_object_url
    
    except Exception as e:
        raise e