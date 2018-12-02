# https://kirr.co/bnk7dx
import boto3

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

# for bucket in s3.buckets.all():
# 	print(bucket.name)


bucket = s3.Bucket(name=AWS_BUCKET_NAME)

for obj in bucket.objects.all(): # Django' Model.objects.all()
	print(obj.key)
	print(obj.Acl().load())


object_key = 'abc/img/Screen Shot 2018-12-02 at 11.58.02 AM.png'
object_acl = s3.ObjectAcl(AWS_BUCKET_NAME, object_key)


