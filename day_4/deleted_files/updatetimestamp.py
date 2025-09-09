import time
import os

file_name = "old_txt_file"
days_old = 40
old_time = time.time() - (days_old * 24 * 60 * 60)

os.utime (file_name , (old_time, old_time))

print(f"Modifiled {file_name} to look {days_old} days_old{time.ctime(old_time)}")
