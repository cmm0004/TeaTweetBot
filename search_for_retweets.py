from auth import API
import tweepy

new_api = API()
api = new_api.authenticate()

print api.me().name
