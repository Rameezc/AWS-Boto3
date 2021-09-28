# This program will list the all the Functions in each Region
# I have permission related issues - So have removed the Region "ap-northeast-3"

import boto3

def list_myfunctions():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    regions = ec2.describe_regions()
    for item in regions['Regions']:
        print('Region ---> : %s ' % item['RegionName'])
        region_name = item['RegionName']
        # Ignore the following Region due to Permissions in my Account.
        if region_name != "ap-northeast-3":
            # Setting Region Name List of Region Names
            client = boto3.client('lambda', region_name=region_name)
            response = client.list_functions()
            functions = response['Functions']
            # If Function is True, Perform the following actions
            if functions:
                count = 0
                print("Please see the functions in the Region below : %s " % region_name)
                print ("=====================================================================")
                for item in functions:
                    count += 1
                    print(count, item['FunctionName'])
                print('\n')
            else:
                print("This Region Has no Functions!")
                print("===============================")
                print('\n')

list_myfunctions()
