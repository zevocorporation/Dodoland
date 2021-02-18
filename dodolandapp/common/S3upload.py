import os
import boto3
from dotenv import load_dotenv

# ENV VARIABLE CONFIGURATION
load_dotenv()

# AWS CREDENTIALS
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
access_region = os.getenv("access_region")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("bucket_name")


def getS3PublicURL(filename):
    try:
        # SETTING UP S3 CREDENTIALS OBJECT
        s3Client = boto3.client('s3', aws_access_key_id=access_key_id,
                                aws_secret_access_key=secret_access_key)

        # FETCHING S3 BUCKET LOCATION
        bucket_location = s3Client.get_bucket_location(Bucket=bucket_name)

        # CREATING PUBLIC URL TO ACCESS IT
        public_object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            bucket_location['LocationConstraint'],
            bucket_name,
            filename)

        return public_object_url

    except Exception as e:
        raise e
