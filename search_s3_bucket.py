# Lambda function in Python 3.8 for searching for files by name in s3 bucket. Takes in two parameters, specifying (1) the bucket, (2) the search term.
# Code was intended to be run using a rest API in API Gateway and requires an IAM role to give lambda access to s3.

import json
import botocore
import boto3

print('loading function...')

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(event['queryStringParameters']['bucket'])
    # list of files that contain the search term
    list_of_filenames = []
    # searches for file based on keys in s3bucket and adds to list
    for obj in bucket.objects.all():
        if not(str(obj.key).endswith('/')) and event['queryStringParameters']['search'] in obj.key.lower().split('/')[-1]: 
            list_of_filenames.append(obj.key)
            
    # response object    
    app_response = {}
    app_response['matching_files'] = list_of_filenames
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)
    
    return responseObject
