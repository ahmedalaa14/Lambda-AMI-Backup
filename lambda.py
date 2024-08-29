import boto3
from datetime import datetime, timedelta
import os

# Create EC2 client 
ec2_client = boto3.client('ec2' , region_name='us-east-1')

# Cerate SNS client
sns_client = boto3.client('sns')

# Get list of all EC2 instances in us-east-1 region
ec2_instances = ec2_client.describe_instances()

# Get list of EC2 instances Ids as list data type
instance_ids = []
for reservation in ec2_instances['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Get the EC2 instance tag having key as 'Name'
for reservation in ec2_instances['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                name_tag = tag['Value']
                break

# Loop the list of instance Ids and create AMI
for instance_id in instance_ids:
    # Add tags to the AMI
    name = ec2_client.describe_tags(Filters=[{'Name': 'resource-id','Values': [instance_id]},{'Name': 'key','Values': ['Name']}])['Tags'][0]['Value']
    now = datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    image_name = f"{name}-{date_string}"
    description = f"AMI for {name} created on {date_string}"
    response = ec2_client.create_image(InstanceId=instance_id, Name=image_name, Description=description, NoReboot=True)
    ami_id = response['ImageId']
    print(f"Created AMI with id {ami_id} for instance {instance_id}")

# Add tags to the AMI
response = ec2_client.create_tags(Resources=[ami_id], Tags=[{'Key': 'Name', 'Value': name_tag}])    

























