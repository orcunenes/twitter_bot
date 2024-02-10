from requests_oauthlib import OAuth1Session
import json

from requests_oauthlib import OAuth1
import requests

def get_media_id(consumer_key, consumer_secret, access_token, access_token_secret):
    # Set up OAuth1 authentication
    auth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # Step 1: Upload media
    media_upload_url = 'https://upload.twitter.com/1.1/media/upload.json'

    with open("MediaUrl", 'rb') as file:
        files = {'media': file}
        media_upload_response = requests.post(media_upload_url, auth=auth, files=files)

    print("Media Upload Response:", media_upload_response.text)

    # Extract media_id from the response
    media_id = json.loads(media_upload_response.text)['media_id']
    print(f'Tweet posted with media ID: {media_id}')

    return media_id





consumer_key = ("")
consumer_secret = ("")

# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)


oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]
uploaded_media_id="test"
uploaded_media_id= get_media_id(consumer_key,consumer_secret,access_token,access_token_secret)
payload = {"text": "Testing!", "media": {"media_ids": [str(uploaded_media_id)]}}




# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.content)
    )

print("Response code: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))







