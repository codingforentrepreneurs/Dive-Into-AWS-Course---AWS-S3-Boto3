import datetime
import os
from conf import IMAGE_DIR, bucket, AWS_BUCKET_NAME, get_s3_client
from utils import DownloadProgressPercentage

file_path = os.path.join(IMAGE_DIR, 'download.png')
key_name = '1.png'




# bucket.download_file('1.png', 
#     file_path, 
#     Callback=DownloadProgressPercentage(file_path))

s3 = get_s3_client()
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params = {
        'Bucket': AWS_BUCKET_NAME,
        'Key': '1.png',
        },
    ExpiresIn= datetime.timedelta(hours=10).total_seconds()
    )

print(url)


# bucket.upload_file(file_path, 
#     '1.png', 
#     ExtraArgs={'ACL': 'public-read'},
#     Callback=UploadProgressPercentage(file_path)
#     )
