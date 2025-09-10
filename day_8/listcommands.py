import subprocess

command = ["cmd", "/c", "dir"]

result = subprocess.run (command , capture_output= True , text= True)

# Print the captured standard output (normal command result)
print("=== Command Output ===")
print(result.stdout)

# Print the captured standard error (if there were errors while running command)
print("=== Command Error (if any) ===")
print(result.stderr)

# Print the exit code (0 = success, non-zero = failure)
print("=== Exit Code ===")
print(result.returncode)
