# This program will list the all the Functions in each Region
# I have 
import boto3

desc_regions = ec2.describe_regions()

for regions in desc_regions['Regions']:
	region_name = regions['RegionName']
	if region_name != "ap-northeast-3":
		client = boto3.client('lambda', region_name=region_name) # you don't need to save to a list and then loop through a list of region names if you can do it here one time!
		response = client.list_functions()
		functions = response['Functions']		
		if functions:  # because you may not have functions in every region
			count = 0
			print 'The Region: %s ' % region_name
			for item in functions:
				count = count + 1
				print count, item['FunctionName']
			print "\n"
count = 1
