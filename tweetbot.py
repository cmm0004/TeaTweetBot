from APIKeys import APIKeys
import tweepy
import sys

api_keys = APIKeys()

auth = tweepy.OAuthHandler(api_keys.consumer_key, api_keys.consumer_secret)
auth.secure = True
auth.set_access_token(api_keys.access_token, api_keys.access_token_secret)
api = tweepy.API(auth)
# If the authentication was successful, you should
# see the name of the account print out
print api.me().name
