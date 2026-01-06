import boto3

def s3_list_buckets(bucket_name):
   
 s3 = boto3.client('s3')

 response = s3.list_objects_v2(Bucket = bucket_name)
 if 'Contents' in response:
     print(f"Objects in bucket '{bucket_name}':")
     for obj in response['Contents']:
         print (f"- {obj['Key']}")
 else:
        print(f"Bucket '{bucket_name}' is empty.")
s3_list_buckets('malli-s3-demo-bkt')




    