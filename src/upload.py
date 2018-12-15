# https://kirr.co/bnk7dx
import os
import requests
from conf import IMAGE_DIR, bucket, AWS_BUCKET_NAME, get_s3_client
from utils import UploadProgressPercentage

file_path = os.path.join(IMAGE_DIR, '1.png')
key_name = '1.png'

fields = {"acl": "public-read"}

conditions = [
    {"acl": "public-read"},
]


s3 = get_s3_client()

post_data = s3.generate_presigned_post(
    Bucket = AWS_BUCKET_NAME,
    Key = 'upload.png',
    Fields=fields,
    Conditions=conditions
)

print(post_data)

# python requests http method post/put/delete/get

with open(file_path, 'rb') as data:
    files = {'file': data}
    url = post_data['url']
    request_data = post_data['fields']
    r = requests.post(url, data=request_data, files=files)
    print(r.status_code) # range of 200 299, 204

# bucket.upload_file(file_path, 
#     '1.png', 
#     ExtraArgs={'ACL': 'public-read'},
#     Callback=UploadProgressPercentage(file_path)
#     )


# with open(file_path, 'rb') as data:
#     bucket.upload_fileobj(data,
#         '1.png',
#         ExtraArgs={'ACL': 'public-read'},
#         Callback=ProgressPercentage(file_path)
#         )

# with open(file_path, 'rb') as data:
#     bucket.put_object(
#         ACL='private',
#         Body= data,
#         Key='1-acl.png'
#         )





