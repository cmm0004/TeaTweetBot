from auth import API
import tweepy
import datetime
from search import Search

new_api = API()
api = new_api.authenticate()



followers = api.followers()
#grab most recent follower
saved_follower = open("./fixtures/most_recent.txt","r+")
if saved_follower == followers[0].screen_name:
    
most_recent=followers[0].
