# https://kirr.co/bnk7dx
from conf import bucket

object_key = 'abc/img/Screen Shot 2018-12-02 at 11.58.02 AM.png'
for obj in bucket.objects.all(): # Django' Model.objects.all()
        print(obj.key)
        if obj.key == object_key:
            obj.Acl().put(ACL='public-read')
        print(obj.Acl().load())



# object_acl = s3.ObjectAcl(AWS_BUCKET_NAME, object_key)

# object_acl.put(ACL='public-read')
# print(object_acl.load())



