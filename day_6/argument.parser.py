import os
import time
import argparse

parser = argparse.ArgumentParser(
    description="Delete files older than specified days in a given directory."
)

parser.add_argument(
    "--path",
    required=True,
    help="Directory path where files need to be checked/deleted"
)

parser.add_argument(
    "--days",
    required= True,
    type=int,
    help="Delete files older than this many days"
)

args = parser.parse_args()

days_in_seconds = args.days * 24* 60 *60
current_time = time.time()

for filename in os.listdir(args.path):
 file_path = os.path.join(args.path, filename)
 if os.path.isfile(file_path):
    file_age = current_time - os.path.getmtime(file_path)
    if file_age > days_in_seconds:
        print(f"Deleting {file_path} (older than {args.days} days)")
        os.remove(file_path)