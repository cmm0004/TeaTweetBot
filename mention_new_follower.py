from auth import API
import tweepy, json, random
from search import Search

new_api = API()
api = new_api.authenticate()

followers = api.followers()
#grab most recent follower
saved_follower = open("./fixtures/most_recent.txt","r+")
if saved_follower.read() != followers[0].user.screen_name:
    fixtures_thx4follow = open("./fixtures/msgs_to_followers.txt", "r")
    lines = open("./fixtures/msgs_to_followers.txt").read().splitlines()
    mention = "@" + str(followers[0].user.screen_name)
    api.update_status(mention + random.choice(lines)) 
    
most_recent=followers[0]

                      
