# Here we will be using Boto to List AWS regions and Loop through each Region to check for AutoScaling Groups!

print 'Listing the Autoscaling Groups in each Region as well as the Launch Configuration'
import boto3

def list_groups():
    client = boto3.client('ec2', region_name='us-east-1')
    regions = client.describe_regions()['Regions']
    # Looping through Region List to create region_name Variable
    for region in regions:
        region_name = region['RegionName']
        # Region Checking/Printing
        print region_name
        print "============================================================="
        # Defining Autoscaling Client and Response
        ec2 = boto3.client('autoscaling', region_name=region_name)
        response = ec2.describe_auto_scaling_groups()['AutoScalingGroups']
        # Checking if there is an Autoscaling Group
        if response:
            count = 0
            desc = ec2.describe_auto_scaling_groups()['AutoScalingGroups'][0]
            groups = desc['AutoScalingGroupName']
            count = count + 1
            launch = desc['LaunchConfigurationName']
            minsize = desc['MinSize']
            maxsize = desc['MaxSize']
            desired = desc['DesiredCapacity']
            print "Number of Autoscaling Groups in the Region: %s " % count
            print "AutoScalingGroups: %s" % groups
            print "Launch Configuration: %s" % launch
            print "Min Group Size: %s" % minsize
            print "Max Group Size: %s" % maxsize
            print "Desire Capacity: %s" % desired
            print "============================================================="
            print
            change_cap = raw_input("Would you like to change Desired Capacity?").lower()
            if change_cap == 'y' or change_cap == 'yes':
                group_name = raw_input('Please enter the Autoscaling Group Name: ')
                desired_cap = int(raw_input('Please enter the Desired Capacity: '))
                if desired_cap < minsize:
                    print "Please note, Desired cannot be less than Min"
            elif change_cap != 'y' or change_cap != 'yes':
                continue
            # Debugging ec2.describe_auto_scaling_groups() Output
            #print desc
            mynewdes = ec2.set_desired_capacity(
                AutoScalingGroupName=group_name,
                DesiredCapacity=desired_cap,
                HonorCooldown=False
            )
        else:
            print 'No Auto Scaling Groups in this Region'
            print


list_groups()

        
         
