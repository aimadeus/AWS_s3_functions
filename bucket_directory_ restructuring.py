# Lambda function in python for moving/restructuring folders in s3 bucket using AWS Cli.
# required layer dependencies: sys, subprocess, and boto3.
# required IAM role for s3 bucket access.

# import packages
import json
import subprocess
import logging

# set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# run AWS CLI command 
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
    # test bucket directory: "icm-testbucket/facilityID1/residents1/residentID1/residentprofile1/"
    bucket_directory = event['bucket_directory']
    
    # old folder structure example: Bucket/facilityID1/residents1/residentID1/residentprofile1/...
    # end goal folder structure: Bucket/residents1/residentprofile1/facilityID1/residentID1/...
    
    # run commands to change bucket structure
    
    run_command('/opt/aws s3 mv %s %s --recursive' % (('s3://icm-testbucket/facilityID1/'), ('s3://icm-testbucket/')))
    run_command('/opt/aws s3 mv %s %s --recursive' % (('s3://icm-testbucket/residents1/residentID1/'), ('s3://icm-testbucket/residents1/')))
    run_command('/opt/aws s3 mv %s %s --recursive' % (('s3://icm-testbucket/facilityID1'), ('s3://icm-testbucket/residents1/residentID1/')))
    run_command('/opt/aws s3 mv %s %s --recursive' % (('s3://icm-testbucket/residents1/residentID1'), ('s3://icm-testbucket/facilityID1/')))
    return('Folders successfully restructured.')
