import os
from pprint import pprint

import requests

BASE_URL = "https://api.notion.com/v1/"


class NotionClient:
    session = requests.Session()

    def __init__(self, token):
        self.session.headers.update({
            'Authorization': f"Bearer {token}",
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
        })

    def get_database(self, database_id):
        response = self.session.get(BASE_URL + f"databases/{database_id}")
        response.raise_for_status()
        return response.json()

    def get_page(self, page_id):
        response = self.session.get(BASE_URL + f"pages/{page_id}")
        response.raise_for_status()
        return response.json()

    def get_user(self):
        response = self.session.get(BASE_URL + f"users")
        response.raise_for_status()
        return response.json()

    def search(self, query):
        response = self.session.post(BASE_URL + "search", json=query)
        response.raise_for_status()
        return response.json()

    def get_page_block(self, page_id):
        response = self.session.get(BASE_URL + f"blocks/{page_id}/children")
        response.raise_for_status()
        return response.json()

# s = NotionClient(os.getenv("NOTION_TOKEN"))
# blocks = s.get_page_block("13c7a047-78d9-80df-9526-e0485f0722cc")
# for block in blocks["results"]:
#     if block["has_children"]:
#         pprint(s.get_page_block(block["id"]))
#         break