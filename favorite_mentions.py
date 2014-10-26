from auth import API
import tweepy
import datetime

new_api = API()
api = new_api.authenticate()

mentions = api.mentions_timeline(None, None, 5, None)
for mention in mentions:
    print mention.id
    try:
        api.create_favorite(526275028388945920)
    except tweepy.TweepError:
        print "You've already favorited that " + str(mention.id)
        continue
    
