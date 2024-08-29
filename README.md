# EC2 AMI Backup Lambda Function
![Lambda-ami](https://user-images.githubusercontent.com/99130650/222965587-d14863b5-e79c-4083-bd56-ff5c3356f7c6.jpeg)

- This project aims to create weekly EC2 AMI backups of all running EC2 instances in the us-east-1 region and delete AMIs older than 30 days.

## Prerequisites
1. Deploy the Lambda Function as per the architecture shown above with required IAM roles.
2. Schedule the Lambda Function to run weekly at 5 AM EST on Sundays using CloudWatch event as the Lambda trigger.
3. Create 5 EC2 instances with Tags as “Name: dpt-web-server”.
4. Create an SNS topic and subscribe an email to receive notifications.

## Description
- This Python code creates Amazon Machine Images (AMIs) for all EC2 instances in the us-east-1 region and deletes unused AMIs older than 30 days. It uses the Boto3 library to interact with the AWS EC2 and SNS APIs.

- The code initializes the EC2 and SNS clients, obtains a list of all EC2 instances in the us-east-1 region, creates an AMI for each instance, and adds tags to identify the AMI's corresponding EC2 instance. The AMI name and description include the instance name and the date of AMI creation.

- After creating the AMI, the code checks if the AMI is older than 30 days and not in use. If both conditions are met, the AMI is deleted.

- The code also sends notifications to an SNS topic if any exceptions occur during the AMI creation or deletion process.

- Deploy this code to an AWS Lambda function and schedule it to run at regular intervals using CloudWatch Events.

## Deployment
- To deploy this code to a Lambda function, follow these steps:

1. Open the AWS Management Console and navigate to the Lambda service.
2. Click the "Create Function" button and choose the "Author from scratch" option.
3. Enter a name for your function and choose "Python 3.9" as the runtime.
4. Under "Permissions", choose "Create a new role with basic Lambda permissions".
5. Click the "Create function" button.
6. In the function editor, paste the code.
7. Set the SNS_TOPIC.