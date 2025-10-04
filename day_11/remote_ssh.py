import paramiko

def remote_ssh_connect (host , port, username, password, command):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect (host, port=port, username=username, password=password)
        print(f"Connected to {host}")
        stdin , stdout, stderr =ssh_client.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        
        if output:
            print("---- Command Output ----")
            print(output)
        if error:
            print("---- Error ----")
            print(error)
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        ssh_client.close()
        print(f"Connection to {host} closed.")
if __name__ == "__main__":
    HOST = ""   # Remote server IP
    PORT = 22                # Default SSH port
    USERNAME = "your_user"
    PASSWORD = "your_password"
    COMMAND = "uptime"
    remote_ssh_connect (HOST, PORT, USERNAME, PASSWORD, COMMAND)
