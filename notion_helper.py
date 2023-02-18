from email import header
import requests
import json
from secrets import *

class NotionClient:
    def __init__(self, database_id, token, default_catagory):
        self.default_catagory = default_catagory
        self.dbid = database_id
        url = f'https://api.notion.com/v1/databases/{database_id}/query'
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"}
        self.headers = headers
        self.database = requests.post(url, headers=headers).json()

    def add(self, name, catagory = None, priority = None, due_date = None, text = None):
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
                "Progress":{
                    "multi_select": [
                        {
                            "name": "Not Started"
                        }
                    ]
                },
            }
        }

        if catagory is not None:
            newPageData["properties"]["Activity"] = {"multi_select": [{"name": catagory}]}
        else:
            newPageData["properties"]["Activity"] = {"multi_select": [{"name": self.default_catagory}]}

        if priority is not None:
            newPageData["properties"]["Priority"] = {"multi_select": [{"name": priority}]}

        if due_date is not None:
            newPageData["properties"]["Due date"] = {"date": {"start": due_date}}
        
        if text is not None:
            newPageData["children"] = [{"paragraph": {"rich_text": [{"text": {"content":text}}]}}]

        data = json.dumps(newPageData)

        result = requests.request("POST", createUrl, headers=self.headers, data=data)

