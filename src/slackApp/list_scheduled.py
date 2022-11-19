#!/usr/bin/env python3

"""Slack messanger."""


import requests
import json
import os
import time

# get secrets
auth_token = os.getenv('auth_token')
channel_id = os.getenv('channel_id')

# Scheduling a message
epoch_time = int(time.time())
headers = {
    'Authorization': f"Bearer {auth_token}",
    'Content-Type': 'application/x-www-form-urlencoded'
}
url = "https://slack.com/api/chat.scheduleMessage"
data = {
    'channel': f"{channel_id}",
    'text': 'Hello World! In 6 minutes',
    'post_at': str(epoch_time+(60*6))
}
response = requests.get(url, headers=headers,params=data)
print("Response: ", json.dumps(response.json(), indent=4))

# Listing all the scheduled messages for the channel
url = "https://slack.com/api/chat.scheduledMessages.list"
data = {'channel': f"{channel_id}"}

response = requests.get(url, headers=headers, params=data)
print("Response: ", json.dumps(response.json()["scheduled_messages"],
                               indent=4))
