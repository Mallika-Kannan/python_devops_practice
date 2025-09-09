import os
import time

folder_path = "C:/Users/2025/Documents/Python/Exercise/python_devops_exercise/day_4/deleted_files"

days_old = 30

current_time = time.time()

cutoff_time =current_time- (days_old * 24 * 60 * 60)

Cutoff_time = time.ctime (cutoff_time)

print (f"Cutoff_time : (File modified before this time are OLD) : {Cutoff_time}")

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path , file_name)

    if os.path.isfile (file_path):
      file_mtime = os.path.getmtime (file_path)

      if file_mtime < cutoff_time :
         print (f"OLD_FILE {file_name} modified at {time.ctime(file_mtime)}")
         os.remove (file_path)

      else : 
         print(f"Recent file: {file_name} (last modified {time.ctime(file_mtime)})")