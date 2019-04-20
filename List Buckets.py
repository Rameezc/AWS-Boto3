import boto3

print 'Here we will be counting and listing all the S3 buckets in the account!'
print

def list_buckets():
    count = 0
    s3_resource = boto3.resource('s3')
    for bucket in s3_resource.buckets.all():
        count = count + 1
        print count, (bucket.name) 

list_buckets()
