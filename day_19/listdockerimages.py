import docker
from docker.errors import DockerException

def list_local_images():
    try:
     client = docker.from_env()

     print ("Fetching images from local")
     images = client.images.list()
     
     if not images:
        print("No image found")
        return
     print(f"{'IMAGE_ID':<15} {'TAGS'}")
     print("-"*60)

     for img in images:
        short_id=img.short_id.split(':')[-1]

        if img.tags:
           tags =img.tags
        else:
           tags = ['<none>:<none>']
        for tag in tags:
           print(f"{short_id:<15} {tag}")
    except DockerException as e:
       print("Docker is not running")
    except Exception as e:
       print (f"unexpected error: {e}")
if __name__ == "__main__":
    list_local_images()
           

