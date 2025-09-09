import psutil

def check_system_health (cpu_threshold=80, memory_threshold=80, disk_threshold=80):

 print ("----System heath check------")

#CPU Usage

 cpu_percent = psutil.cpu_percent(interval=1)
 print(f"CPU_usage: {cpu_percent}%")
 if cpu_percent > cpu_threshold:
  print (f"CPU_usage {cpu_percent}% is high")
 else :
  print (f"CPU_usgae{cpu_percent}% is within limits")


 memory = psutil.virtual_memory()
 memory_percent = memory.percent
 print(f"Memory Usage: {memory_percent}%")
 if memory_percent > memory_threshold:
    print(f"ALERT: Memory usage is high: {memory_percent}% (Threshold: {memory_threshold}%)")
 else:
    print("Memory usage is within normal limits.")

 disk= psutil.disk_usage('/')
 disk_percent = disk.percent
 print(f"Disk Usage ('/'): {disk_percent}%")
 if disk_percent > disk_threshold:
    print(f"ALERT: Disk usage is high: {disk_percent}% (Threshold: {disk_threshold}%)")
 else:
    print("Disk usage is within normal limits.")

    print("--- Health Check Complete ---")

if __name__ == "__main__":
   check_system_health()

 