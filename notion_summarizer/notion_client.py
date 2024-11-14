import os
from pprint import pprint
from notion_formatter import create_notion_page_from_md

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
    
    def create_empty_page(self, parent_page_id, page_name):
        cover =  cover={"type": "external", "external": {"url": "https://ik.imagekit.io/gyzvlawdz/Projects/notion/Stars-6_Ou9B1d2-l.jpg"}}
        properties = {"title": {"title": [{"type": "text", "text": {"content": page_name}}]}}
        payload = dict(parent={"type": "page_id","page_id": parent_page_id}, properties=properties, cover=cover)
        response = self.session.post(BASE_URL + "pages", json=payload)
        response.raise_for_status()
        return response.json()
    
    def update_page(self, page_id, properties):
        payload = dict(properties=properties)
        response = self.session.patch(BASE_URL + f"pages/{page_id}", json=payload)
        response.raise_for_status()
        return response.json()
    
    def append_block(self, page_id, block):
        payload = dict(children=[block])
        response = self.session.patch(BASE_URL + f"blocks/{page_id}/children", json=payload)
        response.raise_for_status()
        return response.json()
        