from email import header
import requests
import json
from secrets import *

class NotionClient:
    def __init__(self, database_id, token):
        self.dbid = database_id
        url = f'https://api.notion.com/v1/databases/{database_id}/query'
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"}
        self.headers = headers
        self.database = requests.post(url, headers=headers).json()

    def add(self, name, catagory, priority = None, due_date = None):
        createUrl = 'https://api.notion.com/v1/pages'
        newPageData = {
            "parent": {"database_id": self.dbid},
            "properties": {
                "Task": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ]
                },
                "Activity":{
                    "multi-select": []
                },
                "Due date":{
                    "date":[]
                },
                "Progress":{
                    "multi-select": []
                },
                "Priority":{
                    "multi-select":[]
                }
            },
            "children":[]
        }

        print(newPageData)

        data = json.dumps(newPageData)

        result = requests.request("POST", createUrl, headers=self.headers, data=data)

        print(result.json())


