import os


def get_env_variable (var_name, default_value= None):
    value = os.environ.get (var_name, default_value)
    return value
def main():
   env_vars = ["PATH", "HOME", "USER", "SHELL", "JAVA_HOME", "MY_CUSTOM_ENV"]
   print (f"Reading env variables")
   for var in env_vars:
      value = get_env_variable (var, default_value="Not Set (Using Default)")
      print (f"{var}:{value}")
   print("\n Setting a new environment variable MY_APP_MODE='development'")
   os.environ["MY_APP_MODE"]="development"
   print(f"MY_APP_NODE",os.environ.get('MY_APP_MODE'))
if __name__ == "__main__":
    main()
    