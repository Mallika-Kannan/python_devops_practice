import boto3

ec2 = boto3.client('ec2')

def stop_ec2_instances():

 response = ec2.describe_instances()
 reservation = response.get ('Reservations',[])
 for r in reservation:
   instance = r.get('Instances')
   for i in instance:
     instance_id = i.get('InstanceId')
     tags = i.get ('Tags',[])
     has_tag = any(t['Key'] == 'env' and t['Value']== 'dev' for t in tags)
     if has_tag:
       print(f"Stopping instance {instance_id} with tag env == dev")
       ec2.stop_instances(InstanceIds=[instance_id])
     else:
       print(f"Instance {instance_id} does not have tag env=dev")
if __name__ == "__main__":
    stop_ec2_instances()
