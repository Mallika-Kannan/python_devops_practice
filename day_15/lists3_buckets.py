import boto3

from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_buckets():
    try:
        print("Creating S3 client...")
        s3_client = boto3.client('s3')
        print("Fetching list of buckets...")
        response = s3_client.list_buckets()
        print(f"Raw response: {response}")
        print ("S3 buckets:")
        for bucket in response ['Buckets']:
            print(f"{bucket['Name']} (Created on: {bucket['CreationDate']})")
    except NoCredentialsError:
        print(f"Wrong AWS credentials")
    except PartialCredentialsError:
        print(f"Incomplete credentials")
    except Exception as e:
        print(f"Error : {str(e)}")
    
if __name__ == "__main__":
    list_s3_buckets()

                                