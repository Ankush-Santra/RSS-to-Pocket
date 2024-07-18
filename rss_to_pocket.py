import feedparser
import requests
import os
import json

POCKET_ADD_URL = "https://getpocket.com/v3/add"
CONSUMER_KEY = os.environ['POCKET_CONSUMER_KEY']
ACCESS_TOKEN = os.environ['POCKET_ACCESS_TOKEN']

# List of RSS feeds with their respective tags
RSS_FEEDS = [
    {"url": "https://www.technologyreview.com/feed", "tag": "Technology"},
    {"url": "https://techcrunch.com/category/artificial-intelligence/feed/", "tag": "AI"},
    # Add more feeds as needed
]

def add_to_pocket(url, title, tags):
    payload = {
        "url": url,
        "title": title,
        "consumer_key": CONSUMER_KEY,
        "access_token": ACCESS_TOKEN,
        "tags": tags
    }
    response = requests.post(POCKET_ADD_URL, json=payload)
    return response.status_code == 200

def process_feed(feed_url, tag):
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        url = entry.link
        title = entry.title
        if add_to_pocket(url, title, tag):
            print(f"Added to Pocket: {title}")
        else:
            print(f"Failed to add to Pocket: {title}")

if __name__ == "__main__":
    for feed in RSS_FEEDS:
        process_feed(feed["url"], feed["tag"])
