from auth import API
import tweepy, json, random
from search import Search

new_api = API()
api = new_api.authenticate()

followers = api.followers()
most_recent = followers[0].screen_name
#grab most recent follower
saved_follower = open("./fixtures/most_recent.txt","r")
s_f = saved_follower.read()
saved_follower.close()

if s_f != most_recent:
    new_saved_follower = open("./fixtures/most_recent.txt","w")
    new_saved_follower.write(most_recent)
    new_saved_follower.close()
    lines = open("./fixtures/msgs_to_followers.txt").read().splitlines()
    mention = "@" + str(most_recent)
    
    api.update_status(mention + " " + random.choice(lines))
    


                      
