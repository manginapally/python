import json
import boto3

def lambda_handler(event, context):
    #to fetch the name of the bucket
    bucket_name= event['Records'][0]['s3']['bucket']['name']
    
    #to fetch the file name
    file_name= event['Records'][0]['s3']['object']['key']
    client = boto3.client('sns')
    
    # to publish the message from sns
    
    client.publish(
        TargetArn = '********************',
        Message = file_name + " A new file has been uploaded to the S3 bucket : " + bucket_name,
        Subject = 'Lambda Activity Detected')
  
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
    
    
    