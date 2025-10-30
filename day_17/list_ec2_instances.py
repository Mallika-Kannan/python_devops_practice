import boto3

def list_ec2_instances():

 try:

   ec2 = boto3.client ('ec2')
   response = ec2.describe_instances()

   print("Listing ec2 instances")

   for reservation in response['Reservations']:
      for instance in reservation ['Instances']:
          instance_id = instance ['InstanceId']
          state = instance ['State']['Name']
          instance_type = instance['InstanceType']
          print(f"Instance ID: {instance_id}, State: {state}, Type: {instance_type}")
   print("\n EC2 instance listing complete.\n")

 except Exception as e:
        print(f" Error: {str(e)}")
if __name__ == "__main__":
     list_ec2_instances()
