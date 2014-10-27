import oauth2
from APIKeys import APIKeys
import time
import urllib2
import json
apikeys = APIKeys()

url1 ="https://api.twitter.com/1.1/search/tweets.json"
params = {"oauth_version":"1.0",
          "oauth_nonce": oauth2.generate_nonce(),
          "oauth_timestamp":int(time.time())
          }

consumer = oauth2.Consumer(key=apikeys.consumer_key,
                           secret=apikeys.consumer_secret)
token = oauth2.Token(key=apikeys.access_token,
                     secret=apikeys.access_token_secret)

params["oauth_consumer_key"] = consumer.key
params["oauth_token"] = token.key

prev_id =int('435458631669415936')

for i in range(1):
    url = url1
    params["q"] ="#tealover"
    params["count"] = 2
    req = oauth2.Request(method="GET", url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, token)
    headers = req.to_header()
    url = req.to_url()
    response = urllib2.Request(url)

    data = json.load(urllib2.urlopen(response))
    print data

