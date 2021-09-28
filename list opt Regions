import boto3

def list_opt_regions():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    regions = ec2.describe_regions()
    for item in regions['Regions']:
        print('Region ----> : %s\n Status: %s ' % (item['RegionName'], item['OptInStatus']))
        print()
        #region_opt = item['OptInStatus']


list_opt_regions()
