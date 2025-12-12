import boto3
from datetime import datetime ,timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def cpu_get_utilization(instance_id):
    end = datetime.utcnow()
    start = end - timedelta(hours =3)
    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start,
        EndTime=end,
        Period=300,
        Statistics=['Average']
    )
    datapoints =metrics.get("Datapoints", [])
    if not datapoints:
        return 0
    avg_cpu = sum(d["Average"] for d in datapoints) / len(datapoints)
    return avg_cpu

def stop_ec2():
    response = ec2.describe_instances()
    reservations =  response.get("Reservations", [])
    for r in reservations:
        instances = r.get("Instances", [])

        for inst in instances:
            instance_id = inst.get("InstanceId")
            tags = inst.get("Tags", [])
            is_dev = any(t['Key'] == 'env' and t['Value'] == 'dev' for t in tags)
           
            if not is_dev:
                print(f"{instance_id} skipped - Not a dev instance")
                continue

            avg_cpu = cpu_get_utilization(instance_id)
            print(f"{instance_id}- Average CPU (last 3 hrs): {avg_cpu:.2f}%")

            if avg_cpu < 5:
                print(f"Stopping {instance_id} (CPU < 5% + tag=dev)")
                ec2.stop_instances(InstanceIds=[instance_id])
            else:
                print(f"{instance_id} is active — not stopping")
if __name__ == "__main__":
    stop_ec2()
