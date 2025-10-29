import boto3

import os

from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3 (file_name, bucket_name, object_name=None):
   if object_name is None: 
      object_name = os.path.basename (file_name)

   s3 = boto3.client ('s3')


   try: 
     print (f"Uploading {file_name} to bucket {bucket_name} as {object_name}")
     s3.upload_file(file_name, bucket_name, object_name)
     print ("upload successful")

   except FileNotFoundError:
     print ("File not found")
   except NoCredentialsError:
     print ("AWS creds not found")
   except ClientError as e:
     print ("Clienterror : {e}")

def main():
   local_file_path =  input ("Enter the local file path: ").strip()
   bucket_name = input ("enter bucket name: ").strip()
   object_name =  input ("enter object name: ").strip()

   upload_to_s3 (local_file_path , bucket_name, object_name)

if __name__ == "__main__":
   main()
 