# https://kirr.co/bnk7dx
import os
from conf import IMAGE_DIR, bucket
from utils import UploadProgressPercentage

file_path = os.path.join(IMAGE_DIR, '1.png')
key_name = '1.png'


bucket.upload_file(file_path, 
    '1.png', 
    ExtraArgs={'ACL': 'public-read'},
    Callback=UploadProgressPercentage(file_path)
    )


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





