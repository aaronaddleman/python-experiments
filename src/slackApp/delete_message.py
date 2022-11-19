#!/usr/bin/env python3
"""Slack messanger."""


import requests
import json
import os

# get secrets
AUTH_TOKEN = os.getenv('auth_token')
CHANNEL_ID = os.getenv('channel_id')

# Sending a message to later on delete
url = "https://slack.com/api/chat.postMessage"
headers = {
    'Authorization': f"Bearer {AUTH_TOKEN}",
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = {
    'channel': '{{CHANNEL_ID}}',
    'text': 'We will delete this message in 10 seconds!🗑'
}
headers = {
    'Authorization': 'Bearer {{AUTH_TOKEN}}',
    'Content-Type': 'application/x-www-form-urlencoded',
}
response = requests.get(url, headers=headers, params=data)
ts = response.json()["ts"]

# Deleting the message
time.sleep(10)
url = "https://slack.com/api/chat.delete"
data = {
    'channel':'{{CHANNEL_ID}}',
    'ts': ts
}
response = requests.get(url, headers=headers,params=data)
print(json.dumps(response.json(), indent=4))
