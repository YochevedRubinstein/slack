import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SlackClient:
    def __init__(self):
        SLACK_OAUTH_TOKEN = os.getenv("SLACK_OAUTH_TOKEN")
        self.client = WebClient(token=SLACK_OAUTH_TOKEN)
        logger.info("Slack client initialized.")

    def get_channels(self):
        try:
            logger.info("Fetching channels...")
            response = self.client.conversations_list()
            logger.info(f"Found {len(response['channels'])} channels.")
            return response['channels']
        except SlackApiError as e:
            logger.error(f"Error fetching channels: {e.response['error']}")
            return []

    def get_users(self):
        try:
            logger.info("Fetching users...")
            response = self.client.users_list()
            logger.info(f"Found {len(response['members'])} users.")
            return response['members']
        except SlackApiError as e:
            logger.error(f"Error fetching users: {e.response['error']}")
            return []

    def send_message(self, channel_id, message):
        try:
            logger.info(f"Sending message to channel {channel_id}...")
            response = self.client.chat_postMessage(channel=channel_id, text=message)
            logger.info(f"Message sent successfully to channel {channel_id}.")
            return response
        except SlackApiError as e:
            logger.error(f"Error sending message to {channel_id}: {e.response['error']}")
            return None

    def create_channel(self, channel_name, is_private=False):
        try:
            logger.info(f"Creating new channel: {channel_name} (Private: {is_private})...")
            response = self.client.conversations_create(name=channel_name, is_private=is_private)
            logger.info(f"Channel '{channel_name}' created successfully.")
            return response
        except SlackApiError as e:
            logger.error(f"Error creating channel '{channel_name}': {e.response['error']}")
            return None

    def add_users_to_channel(self, channel_id, user_ids):
        try:
            logger.info(f"Adding users {user_ids} to channel {channel_id}...")
            response = self.client.conversations_invite(channel=channel_id, users=user_ids)
            logger.info(f"Users {user_ids} added to channel {channel_id} successfully.")
            return response
        except SlackApiError as e:
            logger.error(f"Error adding users to channel {channel_id}: {e.response['error']}")
            return None
