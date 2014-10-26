from APIKeys import APIKeys
import tweepy
import sys

class API(object):
    def __init__(self):
        self.api_keys = APIKeys()
        self.auth = tweepy.OAuthHandler(self.api_keys.consumer_key, self.api_keys.consumer_secret)
        self.auth.secure = True
        self.auth.set_access_token(self.api_keys.access_token, self.api_keys.access_token_secret)

    def authenticate(self):
        
        return tweepy.API(self.auth)


