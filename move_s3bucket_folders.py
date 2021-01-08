# Python Script for moving/restructuring folders in s3 bucket using AWS Cli.
# required dependencies: subprocess and pyyaml (sudo pip3 install pyyaml).

import subprocess
import yaml

with open('/Users/doyoonkim/MyPythonScripts/config.yaml') as file:
    config_info = yaml.full_load(file) #, Loader = yaml.FullLoader)
    
bucket_name = config_info['bucket_name']
old_folder_directory = config_info['old_folder_directory']
new_folder_directory = config_info['new_folder_directory']

def move_folder(bucket_name, old_folder_directory, new_folder_directory):
    # move files in folder to new directory.
    subprocess.call(
        ['aws', 's3', 'mv',
         ('s3://' + bucket_name + old_folder_directory),
         ('s3://' + bucket_name + new_folder_directory),
         '--recursive']
        )
    # cli command: aws s3 mv s3://all-names-are-taken/Facilities/ s3://all-names-are-taken/Residents/Facilities/ --recursive

    # delete old folder
    subprocess.call(
        ['aws', 's3', 'rm',
         ('s3://' + bucket_name + old_folder_directory),
         '--recursive']
        )
    # cli command: aws s3 rm s3://all-names-are-taken/Facilities --recursive
    print('Files successfully moved.')

move_folder(bucket_name, old_folder_directory, new_folder_directory)
