import requests
import json

def fetch_url_json (username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Github user data")
            print(f"Name: {data.get('name')}")
            print(f"Public repos: {data.get('public_repos')} ")
        else:
            print (f"failed to fecth data. status_code:{response.status_code} ")
    except requests.exceptions.RequestException as e:
        print (f"Error occured :{e}")

if __name__ == "__main__":
   fetch_url_json("google")