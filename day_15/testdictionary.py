import boto3

s3_values =boto3.client('s3')
response = s3_values.list_buckets()
print (response)