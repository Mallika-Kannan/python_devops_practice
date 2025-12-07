import os

def list_files():
    folder = input("Enter folder name:")

    if not os.path.exists(folder):
        print("folder not found")
        return
    files = os.listdir(folder)

    txt_count = 0
    log_count = 0
    py_count = 0
    other_count = 0

    for f in files:
        if f.endswith(".txt"):
            txt_count +=1
        elif f.endswith(".log"):
            log_count +=1
        elif f.endswith(".py"):
            py_count +=1
        else:
            other_count+=1
    print("\nFiles in folder:")
    for f in files:
        print(f" - {f}")
    print ("\n Summary:")
    print (f"Text Count: {txt_count}")
    print(f"LOG files  : {log_count}")
    print(f"PY files   : {py_count}")
    print(f"Other files: {other_count}")

if __name__ == "__main__":
   list_files()
        
        
