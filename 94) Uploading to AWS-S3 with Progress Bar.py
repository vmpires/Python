import os
import sys
import threading
import boto3
import json

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

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

s3.upload_file(
    r'C:/Users/50s/Desktop/CV - Victor Milhome Pires (jan-2022).pdf', 'vmpiresbucket1', 'CV-jan-2022',
    Callback=ProgressPercentage(r'C:/Users/50s/Desktop/CV - Victor Milhome Pires (jan-2022).pdf')
)