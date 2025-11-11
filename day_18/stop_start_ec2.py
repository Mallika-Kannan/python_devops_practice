import boto3
import argparse

parser = argparse.ArgumentParser (description= "Stop and start of ec2 instance")
parser.add_argument ("action", choices= ["start","stop"],help ="Action to perfor on ec2")
parser.add_argument("instance_id", help = "Provide instance id")
args= parser.parse_args()

ec2 = boto3.client('ec2')


if args.action == "start":
  print(f"Started instance: {args.instance_id}")
  response = ec2.start_instances(InstanceIds =[args.instance_id])
  print("Response:", response)
elif args.action == "stop":
  print (f"stopping instance {args.instance_id}")
  response = ec2.stop_instances (InstanceIds =[args.instance_id])
  print("Response:", response)