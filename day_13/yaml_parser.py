import yaml
def read_yaml_file(file_path):
    try:
        with open (file_path, 'r') as file: 
            data =  yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"file not found")
    except yaml.YAMLError as e:
        print(f"failed to parse yaml: {e}")
if __name__ == "__main__":
    yaml_file = "config.yaml"
    config_data= read_yaml_file(yaml_file)
    if config_data:
        print (f"YAML file successfully parsed")
        print ("in Python dic")
        print (config_data)
