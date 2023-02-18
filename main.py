from unittest.mock import DEFAULT
from notion_helper import NotionClient
from discord_helper import DiscordClient
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    NOTION_TOKEN = os.getenv('NOTION_TOKEN')
    DATABASE_ID = os.getenv('DATABASE_ID')
    DEFAULT_CATAGORY = os.getenv("DEFAULT_CATAGORY")
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    DISCORD_USERNAME = os.getenv("DISCORD_USERNAME")

    notion_client = NotionClient(DATABASE_ID, NOTION_TOKEN, DEFAULT_CATAGORY)
    discord_client = DiscordClient(DISCORD_USERNAME, notion_client)

    discord_client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()