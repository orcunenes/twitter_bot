import requests
from requests_oauthlib import OAuth1
import json
# Set up your Twitter API credentials
consumer_key = 'jf40LBwOWKU3CtCDARhasY8Ps'
consumer_secret = '0ckAJUJR7QFh0vyySnlowbXb1jQwAWEYmIYfRHMISMyvQY2Cr0'
access_token = '1692964396211884033-hAlo4bge4NMpd8URSVKAtqcdoEC7Yf'
access_token_secret = 'N7P8fU0jfIYhUYmTvWhTQaCBLSR8mI0EFjohbB9xeF8fl'
# Set up OAuth1 authentication
auth = OAuth1(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret
)

# Step 1: Upload media
media_upload_url = 'https://upload.twitter.com/1.1/media/upload.json'
file_path = 'C:\\Users\\orcun\\OneDrive\\Masaüstü\\memes\\image.png'

with open(file_path, 'rb') as file:
    files = {'media': file}
    media_upload_response = requests.post(media_upload_url, auth=auth, files=files)

print("Media Upload Response:", media_upload_response.text)

# Step 2: Post a tweet with the attached media
tweet_text = 'Hello, Twitter! This is my image.'
update_status_url = 'https://api.twitter.com/1.1/statuses/update.json'
params = {'status': tweet_text, 'media_ids': media_upload_response.text}
response = requests.post(update_status_url, auth=auth, params=params)

print(f'Tweet posted with media ID: {media_upload_response.text}')