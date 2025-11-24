import requests
import os

def send_slack_message(webhook_url, message):
    payload = {"text" : message}
    response =  requests.post(webhook_url, json = payload)
    
    print(f"Status: {response.status_code}, Response: {response.text}")
if __name__ == "__main__":
    
    WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
    MESSAGE = "Hello from my slack python script"

    send_slack_message(WEBHOOK_URL, MESSAGE)
    
       