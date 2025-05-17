Great! Here are some Python-based AWS Lambda coding questions and mini-projects you may face in interviews or use for practice:


---

1. Basic Lambda Function to Reverse a String

Question:
Write a Lambda function in Python that takes a string from the event and returns the reversed string.

Solution:

def lambda_handler(event, context):
    input_str = event.get('input', '')
    reversed_str = input_str[::-1]
    return {
        'statusCode': 200,
        'body': reversed_str
    }


---

2. Lambda Function to Write Data to DynamoDB

Question:
Write a Lambda function that inserts name and email from the event into a DynamoDB table.

Solution:

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    name = event['name']
    email = event['email']

    table.put_item(Item={'name': name, 'email': email})

    return {
        'statusCode': 200,
        'body': 'User added successfully'
    }


---

3. Lambda to Trigger on S3 Upload and Log File Name

Question:
Create a Lambda that triggers when a file is uploaded to an S3 bucket and logs the file name.

Solution:

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"New file uploaded: {key} in bucket {bucket}")


---

4. Lambda Scheduled Job (Cron) – Clean Up Unused EBS Volumes

Mini-project: Write a Lambda function triggered by EventBridge every day to find and print unattached EBS volumes.

Solution:

import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )

    for vol in volumes['Volumes']:
        print(f"Unused volume: {vol['VolumeId']}")


---

5. Lambda with SNS Notification on EC2 Start

Mini-project: Write a Lambda that is triggered on EC2 instance start and sends an email using SNS.

Solution:

import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    message = f"EC2 Instance {instance_id} has started."

    sns.publish(
        TopicArn='arn:aws:sns:your-region:account-id:your-topic',
        Subject='EC2 Start Notification',
        Message=message
    )


---

Want more real-world mini Lambda projects?

I can give you:

Lambda to consolidate security group rules and send report

Lambda to auto-tag AWS resources

Lambda for cost optimization

Lambda that receives HTTP requests via API Gateway and stores logs in DynamoDB


Let me know which type you'd like!

