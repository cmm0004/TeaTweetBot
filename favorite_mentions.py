from auth import API
import tweepy
import datetime

new_api = API()
api = new_api.authenticate()


mentions = api.mentions_timeline()
for mention in mentions:
    try:
        api.create_favorite(mention.id)
    except tweepy.TweepError:
        print "You've already favorited that " + str(mention.id)
        continue
    
