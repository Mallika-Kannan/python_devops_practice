import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

def list_tags():
  for reservation in response.get("Reservations", []):
    for instance in reservation.get("Instances", []):
      instance_id = instance.get("InstanceId")
      state = instance.get("State",{}).get ("Name")
      tags = instance.get("Tags", [])
      print(f"Instance ID: {instance_id}")
      print(f"State: {state}")
      if tags: 
        for tag in tags:
          print (f"Tag is {tag ['Key']}| Value: {tag['Value']}")
      else:
          print ("No tags found")
      print("-" * 40)


if __name__== "__main__":
 list_tags()