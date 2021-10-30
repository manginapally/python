import json
import boto3

def lambda_handler(event, context):
    
    sqs_client = boto3.client('sqs')
    sqs_url = '***********************'
   
    sqs_client.send_message(QueueUrl = sqs_url, MessageBody = json.dumps(event))
   
   
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
