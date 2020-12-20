# working lambda function for calculating the size of S3 bucket. Requires IAM role access to S3.

import boto3
import botocore
import json

print('loading function...')

def lambda_handler(event, context):
    # access bucket, calculate total size
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(event['queryStringParameters']['bucket'])
    total_bytes = 0
    bytes_to_mb = 0.000001
    for key in bucket.objects.all():
        total_bytes += key.size
    bucket_size = total_bytes * bytes_to_mb
    
    # app response
    app_response = {}
    app_response['bucket_size'] = 'total size of folder is ' + str(bucket_size) + '.'
    
    # response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)
    
    return responseObject
