import os
from conf import IMAGE_DIR, bucket
from utils import DownloadProgressPercentage

file_path = os.path.join(IMAGE_DIR, 'download.png')
key_name = '1.png'



bucket.download_file('1.png', 
    file_path, 
    Callback=DownloadProgressPercentage(file_path))


# bucket.upload_file(file_path, 
#     '1.png', 
#     ExtraArgs={'ACL': 'public-read'},
#     Callback=UploadProgressPercentage(file_path)
#     )
