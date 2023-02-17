from notion_helper import NotionClient
from secrets import *

def main():
    print('a')
    client = NotionClient(DATABASE_ID, TOKEN)
    client.add("test", "high")

if __name__ == "__main__":
    main()