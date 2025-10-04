import requests

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.nonexistentwebsiteexample123.com" 
]

for url in urls: 
    try:
        response = requests.get (url , timeout=5)
        if response.status_code==200:
         print(f"{url} is accessible")
        else:
         print(f"[WARN] {url} returned status code {response.status_code}")
    except requests.exceptions.RequestException as e :
      print(f"[ERROR] Could not access {url} - Reason: {e}")
        