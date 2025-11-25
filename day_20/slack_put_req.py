import requests
import os

def slack_send_message(webhook_url,message):
    payload = {"text": message}
    response = requests.post(webhook_url,json = payload)
    if response.status_code == 200:
     print ("Message sent")
    else:
     print (f"Message not sent",response.text)

if __name__ == "__main__":
    webhookurl = os.getenv ("SLACK_WEBHOOKURL")
    MESSAGE = "Hello from python script"
    slack_send_message(webhookurl,MESSAGE)