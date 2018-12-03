# https://kirr.co/bnk7dx
import boto3
import os
import sys
import threading


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




class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()



# bucket.upload_file(file_path, 
#     '1.png', 
#     Callback=ProgressPercentage(file_path)
#     )


# with open(file_path, 'rb') as data:
#     bucket.upload_fileobj(data,
#         '1.png',
#         Callback=ProgressPercentage(file_path)
#         )

with open(file_path, 'rb') as data:
    bucket.put_object(
        ACL='private',
        Body= data,
        Key='1-acl.png'
        )





