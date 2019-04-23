import boto3

print 'Here we will check the various AWS Regions for Instances and Print the Region along with Instance ID'

def region_names():
    region_list = []
    ec2 = boto3.client('ec2', region_name='us-east-1')
    region = ec2.describe_regions()
    # Placing Regions in a List
    for item in region['Regions']:
        region_list.append(item['RegionName'])
        # Redefine Region and Region Name as List of Names
    for name in region_list:
        region = boto3.client('ec2', region_name=name)
        # Checking if there is an Instance
        if region.describe_instances()['Reservations']:
            desc = region.describe_instances()['Reservations'][0]['Instances'][0]
            # Print Instance ID, Private IP and Private DNS Name
            Id = desc['InstanceId']
            Ip = desc['PrivateIpAddress']
            dns = desc['PrivateDnsName']
            print 'Region: %s ' % name
            print '=================='
            print 'Instance Details:'
            print '=================='
            print Id
            print Ip
            print dns
            print '==================='
            print 

region_names()
