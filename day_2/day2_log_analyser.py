import sys

def analyser_log_file (log_file_path) :

 error_lines = []
 error_count = 0
 try: 
  with open (log_file_path ,'r') as file: 
     for line in file :
       if "ERROR" in line :
         error_count += 1
         error_lines.append(line.strip())

 except FileNotFoundError :
   print(f"Error: The file '{log_file_path}' was not found.")
   return 

 except exception as e:
   print(f"Error found {e}")
   return

 print(f"Log analysis complete for file: '{log_file_path}'")
 print("-" * 40)

 if error_count > 0 :
   print (f"Found {error_count} errors")
   print (f"details of error")
   for error_line in error_lines :
      print (f" - {error_line}")
 else:
        print("No lines containing 'ERROR' were found.")

if __name__ == "__main__" : 
  if len(sys.argv) < 2 : 
     print ("USage :python day2_log_analyzer.py <path_to_log_file> ")
  else: 
     log_file = sys.argv[1]
     analyser_log_file(log_file)

 



