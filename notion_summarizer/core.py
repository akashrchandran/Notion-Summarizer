import os

from dotenv import load_dotenv
from gemini import GeminiClient
from notion_client import NotionClient
from utils import get_vtt_file_from_url, prompt_formater
from notion_formatter import parse_md

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

notion_client = NotionClient(NOTION_TOKEN)
gemini_client = GeminiClient(GEMINI_TOKEN)





blocks = notion_client.get_page_block(PAGE_ID)["results"]
for block in blocks[8:]:
    if block["has_children"]:
        children = notion_client.get_page_block(block["id"])["results"]
        for child in children:
            if child["type"] == "file" and child["file"]["name"].endswith(".vtt"):
                file_url = child["file"]["file"]["url"]
                file_content = get_vtt_file_from_url(file_url)
                prompt = prompt_formater(file_content)
                summary = gemini_client.generate_content(prompt)
                new_page = notion_client.create_empty_page(block["id"], "(AI GENERATED SUMMARY) " + block["child_page"]["title"])
                for container in parse_md(summary):
                    notion_client.append_block(new_page["id"], container)