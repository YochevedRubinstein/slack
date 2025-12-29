import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_OAUTH_TOKEN = os.getenv("SLACK_OAUTH_TOKEN")
client = WebClient(token=SLACK_OAUTH_TOKEN)

def get_channels():
    try:
        response = client.conversations_list()
        channels = response['channels']
        
        print("Channels in Slack workspace:")
        for channel in channels:
            print(f"Channel name: {channel['name']} (ID: {channel['id']})")
    except SlackApiError as e:
        print(f"Error fetching channels: {e.response['error']}")

def get_users():
    try:
        response = client.users_list()
        users = response['members']
        
        print("\nUsers in Slack workspace:")
        for user in users:
            print(f"User: {user['name']} (ID: {user['id']})")
    except SlackApiError as e:
        print(f"Error fetching users: {e.response['error']}")

def send_message(channel_id, message):
    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        print("\nMessage sent successfully!")
        print(response)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

def create_channel(channel_name, is_private=False):
    try:
        response = client.conversations_create(
            name=channel_name,
            is_private=is_private
        )
        print(f"Channel '{channel_name}' created successfully!")
        print(response)
    except SlackApiError as e:
        print(f"Error creating channel: {e.response['error']}")

def add_users_to_channel(channel_id, user_ids):
    try:
        response = client.conversations_invite(
            channel=channel_id,
            users=user_ids
        )
        print(f"Users added to channel {channel_id} successfully!")
        print(response)
    except SlackApiError as e:
        print(f"Error adding users to channel: {e.response['error']}")

def main():
    get_channels()
    get_users()
    
    send_message("C1234567890", "Hello from my Slack bot!")
    
    create_channel("new-channel", is_private=True) 
    
    add_users_to_channel("C1234567890", ["U12345678", "U87654321"]) 

if __name__ == "__main__":
    main()
