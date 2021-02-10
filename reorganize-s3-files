# Lambda function in python for moving/restructuring folders in s3 bucket using AWS Cli commands.
# required AWS layer.
# required IAM role for s3 bucket access.

import json
import subprocess
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def run_command(command):
    command_list = command.split(' ')
    try:
        logger.info("Running shell command: \"{}\"".format(command))
        result = subprocess.run(command_list, stdout=subprocess.PIPE);
        logger.info("Command output:\n---\n{}\n---".format(result.stdout.decode('UTF-8')))
    except Exception as e:
        logger.error("Exception: {}".format(e))
        return False
    return True

def lambda_handler(event, context):
    body = json.loads(event['body'])
    bucket_name = body['bucket_name']
    old_folder_directory = body['old_folder_directory']
    new_folder_directory = body['new_folder_directory']
    
    # run command to move file or folder.
    run_command('/opt/aws s3 mv %s %s --recursive' % (('s3://' + bucket_name + old_folder_directory), ('s3://' + bucket_name + new_folder_directory)))  
    
    # app response
    app_response = {}
    app_response['file'] = 'files successfully moved from.'
    
    # response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)
    return responseObject
