import os
import requests

token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError ("Token missing! Run export: GITHUB_TOKEN: your_token")

username = input ("Enter Github username:")

url = f"https://api.github.com/users/{username}/repos"

headers = {
    "Authorization" : f"token {token}",
    "Accept":"application/vnd.github+json"
}

response = requests.get (url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    print (f"\n Public_repos for {username}: \n")

    for repo in repos: 
        print (repo['name'])
else:
    print (f"Error: {response.status_code}- {response.text}")

