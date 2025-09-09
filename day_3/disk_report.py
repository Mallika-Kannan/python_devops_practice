import shutil
import sys

THRESHOLD_PERCENT = 80.0
PATH_TO_CHECK= '/'

def check_disk_usage (path, threshold): 
 try: 
  total,used,free = shutil.disk_usage(path)
  percent_used = (used/total) * 100

  message = (
   f"Disk usage for {path}: \n"
   f"  Total : {total // (1024 ** 3)} GB\n"
   f"  Used : {used // (1024 ** 3)} GB ({percent_used:.2f}%)\n"
   f" free : {free // (1024 ** 3)} GB\n"
  )
  print (message)

  if percent_used > threshold :
    print (f" \n WARNING Disk usage ({percent_used:.2f}% is baove threshold {threshold}%.")
    sys.exit(1)
  else : 
    print (f"\n disk usage is within limit")
    sys.exit(0)
 except FileNotFoundError:
   print(f"[ERROR] The path '{path}' was not found.", file=sys.stderr)
   sys.exit(2) 
 except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(3)

if __name__ == "__main__":
    check_disk_usage(PATH_TO_CHECK, THRESHOLD_PERCENT)
