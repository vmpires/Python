import boto3
from botocore.exceptions import ClientError
import json
import logging

# Getting user + pass from external file
f = open ('config.json', 'r')
key = json.load(f)

usuario = key['senhas'][1]['user']
senha = key['senhas'][1]['pass']

# Creates the service with AWS credentials
s3 = boto3.client(
    service_name = 's3',
    region_name = 'sa-east-1',
    aws_access_key_id = usuario,
    aws_secret_access_key = senha
)

# Uploads selected file to S3 Bucket
try:
    response = s3.upload_file(r'C:/Users/50s/Desktop/CV - Victor Milhome Pires (jan-2022).pdf', 'vmpiresbucket1', 'CV-jan-2022')
except ClientError as e:
    logging.error(e)
    print(f"File cannot be uploaded: {e}")

