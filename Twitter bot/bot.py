import tweepy
import requests
import json
import time

# Twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# HN endpoint to get the latest stories
hn_url = "https://hacker-news.firebaseio.com/v0/newstories.json"

# Get the list of story ids
hn_response = requests.get(hn_url)
story_ids = json.loads(hn_response.text)

# Iterate through the stories
for story_id in story_ids:
    # Get the details of the story
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_response = requests.get(story_url)
    story_details = json.loads(story_response.text)

    # Extract the title and URL of the story
    story_title = story_details['title']
    story_link = story_details.get('url', story_details.get('text', None))
    # Handle cases where the story does not have a URL
    if story_link is None:
        continue
    # Post the story to Twitter
    tweet = f"{story_title} {story_link}"
    api.update_status(status=tweet)
    time.sleep(600)
