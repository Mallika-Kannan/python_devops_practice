import boto3
import argparse

parser = argparse.ArgumentParser (description= "stop/start ec2")
parser.add_argument("action", choices = ["start","stop"], help = "enter the action")
parser.add_argument("instance_ids", nargs="+", help = "enter ec2 instanceids" )
args = parser.parse_args()

ec2 = boto3.client('ec2')

response = ec2.describe_instances(InstanceIds=args.instance_ids)

instances=[]
for reservation in response ["Reservations"]:
    for instance in reservation ["Instances"]:
        instances.append({
            "InstanceId": instance["InstanceId"],
            "State" : instance["State"]["Name"]
        })
for inst in instances:
    instance_id = inst["InstanceId"]
    State = inst ["State"]

    if args.action == "start":
      if State == "running":
       print ("ec2 is already running")
      else: 
       print(f"starting instance {instance_id}, state :{State}")
       ec2.start_instances(InstanceIds =[instance_id])
       print ("Instance started")
    elif args.action == "stop":
      if State == "stopped":
       print ("ec2 is stopped already")
      else:
       print (f"Stopping instance{instance_id}, state :{State}")
       ec2.stop_instances(InstanceIds =[instance_id])
       print("instance_stopped")
