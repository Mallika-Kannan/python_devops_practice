import requests

def send_slack_message(webhook_url, message):
    payload = {"text" : message}
    response =  requests.post(webhook_url, json = payload)
    if response.status_code ==200:
        print("Message sent successfully")
    else:
        print ("Message not sent", response.txt)
if __name__ == "__main__":
    
    WEBHOOK_URL = "https://hooks.slack.com/services/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"
    MESSAGE = "Hello from my slack python script"

    send_slack_message(WEBHOOK_URL, MESSAGE)
    
       