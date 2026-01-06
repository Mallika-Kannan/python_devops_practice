import boto3

def s3_list_all_buckets():
   
 s3 = boto3.client('s3')
 response = s3.list_buckets() 
 

 for bucket in response['Buckets']:
  bucket_name =bucket['Name']    
  print (f"Buckets in the account are {bucket_name}") 
  response_obj = s3.list_objects_v2(Bucket = bucket_name)
  if 'Contents' in response_obj:
     print(f"Objects in bucket '{bucket_name}':")
     for obj in response_obj['Contents']:
         print (f"- {obj['Key']}")
s3_list_all_buckets()
 

 
