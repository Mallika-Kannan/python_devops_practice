import psutil 

def check_process (process_name): 
    for process in psutil.process_iter (['pid' , 'name']):
        if process_name.lower() in process.info ['name'].lower():
            return True
    return False

if __name__ == "__main__":
 process_to_check = input ("Enter the process name").strip()
 if check_process (process_to_check):
    print(f"The process '{process_to_check}' is running.")
 else : 
    print(f"The process '{process_to_check}' is NOT running.")


