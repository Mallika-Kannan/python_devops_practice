import boto3

ec2 = boto3.client('ec2')

ec2_inst = ec2.describe_instances()

def stop_ec2_instance():

 reservation = ec2_inst.get['Reservations']
 for r in reservation:
    instance = reservation.get['Instances'] 
    for i in instance:
        instanceid = i.get['InstanceId']
        tag = i.get['Tags']
        if tag not exist:
          print ("No instances with specified tags")
        else:
          t = tag.get[{'Key','env'}| {'Value', 'dev'}]
          print ("Stopping instances with tag as dev")

if __name__ == "__main__":
   stop_ec2_instance()