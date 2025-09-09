import os
import shutil
import datetime

SOURCE_DIR = r"C:\Users\2025\Documents\Python\Exercise\python_devops_exercise\day_1\my_app"

DESTINATON_DIR = r"C:\Users\2025\Documents\Python\Exercise\python_devops_exercise\day_1\backups_storage"

current_date = datetime.date.today().strftime("%Y-%m-%d")
backup_folder_name = f"backup-{current_date}"
destination_path = os.path.join (DESTINATON_DIR , backup_folder_name) 

try : 
    if not os.path.exists (SOURCE_DIR) :
     print (f"Error : Source directory '{SOURCE_DIR}' doesn't exists")
    else :  
     shutil.copytree (SOURCE_DIR ,destination_path)
     print (f"successfully created backup of '{SOURCE_DIR}' at '{destination_path}'")
except FileExistsError : 
      print(f"Backup directory '{destination_path}' already exists. No action taken.")
except Exception as e :
       print(f"An error occurred: {e}")