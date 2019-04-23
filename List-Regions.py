import boto3

print 'Here we will be listing all the AWS Regions!'
print

def list_regions():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    regions = ec2.describe_regions()
    for item in regions['Regions']:
        print 'Region ---> : %s ' % item['RegionName']

list_regions()

