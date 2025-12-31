from slack_api import SlackClient

def main():
    slack_client = SlackClient()
    channels = slack_client.get_channels()
    users = slack_client.get_users()
    slack_client.send_message("C1234567890", "Hello from my Slack bot!")
    slack_client.create_channel("new-channel", is_private=True)
    slack_client.add_users_to_channel("C1234567890", ["U12345678", "U87654321"])

if __name__ == "__main__":
    main()
