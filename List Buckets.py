import boto3
s3 = boto3.resource('s3')

print 'Here we will be counting and listing all the S3 buckets in the account!'
print 

count = 1
for bucket in s3.buckets.all():
  count += 1
  print count, (bucket.name)
  
