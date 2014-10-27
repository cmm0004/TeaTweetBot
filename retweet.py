from auth import API
import tweepy
import datetime
import json
new_api = API()
api = new_api.authenticate()

from search import Search
search = Search("#tealover", 4)
json = search.search()

print json
