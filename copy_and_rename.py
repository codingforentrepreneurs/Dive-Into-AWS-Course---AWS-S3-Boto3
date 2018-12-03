import os
import requests
from conf import IMAGE_DIR, bucket, AWS_BUCKET_NAME

copy_source = {
    'Bucket': AWS_BUCKET_NAME,
    'Key': 'upload.png'
}


obj = bucket.Object('uploads/2.png')
obj.copy(copy_source)

old_obj = bucket.Object('upload.png').delete()
