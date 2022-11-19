#!/usr/bin/env python3
"""Slack messanger."""


import requests
import json
import os

# get secrets
auth_token = os.getenv('auth_token')
channel_id = os.getenv('channel_id')

# Sending a message
headers = {
    'Authorization': f"Bearer {auth_token}",
    'Content-Type': 'application/x-www-form-urlencoded',
}
url = "https://slack.com/api/chat.postMessage"
data = {
    'channel': f"{channel_id}",
    'text': 'This message will be updated!'
}
response = requests.get(url, headers=headers, params=data)
print("response: ", json.dumps(response.json(), indent=4))

# Updating the message we sent before
url = "https://slack.com/api/chat.update"
data = {
    'channel': f"{channel_id}",
    'ts': response.json()['ts'],
    'text': 'This is an updated message!'
}
response = requests.get(url, headers=headers, params=data)
print(json.dumps(response.json(), indent=4))
