# https://kirr.co/bnk7dx
import os
from conf import IMAGE_DIR, bucket, AWS_BUCKET_NAME, get_s3_client
from utils import UploadProgressPercentage

file_path = os.path.join(IMAGE_DIR, '1.png')
key_name = '1.png'


s3 = get_s3_client()

post_data = s3.generate_presigned_post(
    Bucket = AWS_BUCKET_NAME,
    Key = 'upload.png'
)

print(post_data)


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





