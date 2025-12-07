import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
def list_s3_buckets():
 try:
   s3_var = boto3.client('s3')
   responses = s3_var.list_buckets()

   for bucket in responses['Buckets']:

    print (f"Bucket_name: {bucket['Name']}")
 except NoCredentialsError:
   print("Invalid creds")

if __name__ == "__main__":
 list_s3_buckets()
  
   
   
   
  
  
