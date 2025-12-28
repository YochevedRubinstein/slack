import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SLACK_OAUTH_TOKEN = os.getenv("SLACK_OAUTH_TOKEN")

headers = {
    "Authorization": f"Bearer {SLACK_OAUTH_TOKEN}",
}

def get_channels():
    url = "https://slack.com/api/conversations.list"
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        channels = response.json().get("channels", [])
        if response.json().get('ok'):
            print("Channels in Slack workspace:")
            for channel in channels:
                print(f"Channel name: {channel['name']} (ID: {channel['id']})")
        else:
            print(f"Error fetching channels: {response.json().get('error')}")
    else:
        print(f"Error fetching channels: {response.status_code}")

def get_users():
    url = "https://slack.com/api/users.list"
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        users = response.json().get("members", [])
        if response.json().get('ok'):
            print("\nUsers in Slack workspace:")
            for user in users:
                print(f"User: {user['name']} (ID: {user['id']})")
        else:
            print(f"Error fetching users: {response.json().get('error')}")
    else:
        print(f"Error fetching users: {response.status_code}")

def send_message(channel_id, message):
    message_url = "https://slack.com/api/chat.postMessage"
    message_data = {
        "channel": channel_id, 
        "text": message
    }
    message_response = requests.post(message_url, headers=headers, json=message_data, verify=False)
    
    if message_response.status_code == 200:
        print("\nMessage sent successfully!")
        print(message_response.json())
    else:
        print(f"Error sending message: {message_response.status_code}")

def main():
    get_channels()
    get_users()
    send_message("C1234567890", "Hello from my Slack bot!")

if __name__ == "__main__":
    main()
