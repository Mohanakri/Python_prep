Here are some common AWS Lambda interview questions along with their answers, tailored for a Python developer like you:


---

1. What is AWS Lambda?

Answer: AWS Lambda is a serverless compute service that lets you run code in response to events (like API calls, file uploads, cron jobs) without provisioning or managing servers. You only pay for the compute time you use.


---

2. What are the key features of Lambda?

Answer:

No server management

Automatic scaling

Millisecond billing

Event-driven execution

Supports multiple languages (Python, Node.js, etc.)

Easily integrates with AWS services (S3, DynamoDB, API Gateway, etc.)



---

3. What triggers Lambda functions?

Answer: Lambda functions can be triggered by:

API Gateway (REST API)

S3 (e.g., object created)

CloudWatch (cron jobs or alarms)

DynamoDB Streams

SNS/SQS

EventBridge

Cognito, CloudFormation, etc.



---

4. How do you write a basic Lambda function in Python?

Answer:

def lambda_handler(event, context):
    print("Received event:", event)
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }


---

5. What is the use of the context object in Lambda?

Answer: context provides runtime information about the Lambda function:

context.function_name

context.memory_limit_in_mb

context.aws_request_id

context.get_remaining_time_in_millis()



---

6. What is the maximum timeout for a Lambda function?

Answer: The maximum execution timeout is 15 minutes (900 seconds).


---

7. How do you pass data to a Lambda function?

Answer: Via the event parameter. For example, if triggered by API Gateway, event will contain query strings, headers, etc.


---

8. Can Lambda be stateful?

Answer: No, Lambda is stateless. However, you can persist state externally using DynamoDB, S3, or RDS.


---

9. What are cold starts in Lambda?

Answer: Cold start occurs when Lambda needs to initialize a new container for the first request. This adds a small delay (especially for VPC-based Lambdas). Subsequent requests reuse the container (warm start).


---

10. How do you deploy Lambda code?

Answer:

AWS Console (inline editor or upload ZIP)

AWS CLI / SAM / CDK / Terraform

CI/CD pipelines

From S3 bucket (ZIP file)



---

11. How can you monitor Lambda functions?

Answer: Using:

CloudWatch Logs (automatic log collection)

CloudWatch Metrics (invocation count, duration, error rate)

X-Ray for tracing



---

12. Can Lambda functions access VPC resources?

Answer: Yes. You must configure the Lambda to run in a VPC and assign subnets + security groups. Keep in mind this may increase cold start times.


---

13. What is the Lambda execution role?

Answer: An IAM role that gives Lambda permission to interact with other AWS services (like reading from S3 or writing to DynamoDB).


---

14. What is Lambda Layers?

Answer: Lambda Layers let you package common dependencies (e.g., Python libraries) and reuse them across multiple Lambda functions.


---

15. What is AWS SAM or Serverless Framework?

Answer: These are frameworks to define and deploy serverless applications using templates and CLI:

AWS SAM (Serverless Application Model): uses template.yaml

Serverless Framework: uses serverless.yml



---

Would you like Python-based coding questions or mini-projects related to Lambda too?

