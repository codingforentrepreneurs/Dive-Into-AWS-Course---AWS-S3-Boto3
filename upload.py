# https://kirr.co/bnk7dx
import boto3
import os

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

AWS_ACCESS_KEY_ID = 'AKIAIPCQFHKC4E4EZ62A' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_DEFAULT_REGION = 'us-east-1'
AWS_BUCKET_NAME = 'aws-cfe-intro'

session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_DEFAULT_REGION
    )

s3 = session.resource("s3")

bucket = s3.Bucket(name=AWS_BUCKET_NAME)

file_path = os.path.join(IMAGE_DIR, '1.png')
key_name = '1.png'
bucket.upload_file(file_path, '1.png', Callback=)




