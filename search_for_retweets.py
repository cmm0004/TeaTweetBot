from auth import API
import tweepy
import datetime

new_api = API()
api = new_api.authenticate()

mentions = api.mentions_timeline()
print mentions


##while True:
##    time = datetime.now()
##    
##retweets = api.retweets_of_me(None, None, 5, None)
##for tweet in retweets:
##    print tweet.id


