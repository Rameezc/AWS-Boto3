import boto3
# The Purpose of this code is to Describe all Regions and Instances Running in each Region

# Define the Client - EC2

ec2 = boto3.client('ec2', region_name='us-east-1')

# Define the Empty Region List - To be used later.

regionlist = []
regions = ec2.describe_regions()

# Get the Region Names and Store in the regionlist[]

for item in regions['Regions']:
    regionlist.append(item['RegionName'])

# For each Region in Region-List, perform region.describe_instances(), Filtering for Instance ID 

for name in regionlist:
    region = boto3.client('ec2', region_name=name)
    if region.describe_instances()['Reservations']:
        desc = region.describe_instances()['Reservations'][0]['Instances'][0]
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
