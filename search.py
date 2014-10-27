import oauth2
from APIKeys import APIKeys
import time
import urllib2
import json


class Search(object):

    def __init__(self, query, count):
        self.apikeys = APIKeys()
        self.query = query
        self.count = count
        self.apikeys = APIKeys()
        self.url1 ="https://api.twitter.com/1.1/search/tweets.json"
        self.params = {"oauth_version":"1.0",
                  "oauth_nonce": oauth2.generate_nonce(),
                  "oauth_timestamp":int(time.time())
                  }

        self.consumer = oauth2.Consumer(key=self.apikeys.consumer_key,
                                   secret=self.apikeys.consumer_secret)
        self.token = oauth2.Token(key=self.apikeys.access_token,
                             secret=self.apikeys.access_token_secret)

        self.params["oauth_consumer_key"] = self.consumer.key
        self.params["oauth_token"] = self.token.key
        
    def search(self):
        
        for i in range(1):
            url = self.url1
            self.params["q"] = self.query
            self.params["count"] = self.count
            req = oauth2.Request(method="GET", url=url, parameters=self.params)
            signature_method = oauth2.SignatureMethod_HMAC_SHA1()
            req.sign_request(signature_method, self.consumer, self.token)
            headers = req.to_header()
            url = req.to_url()
            try:
                response = urllib2.Request(url)

                data = json.load(urllib2.urlopen(response))
                return data
            except urllib2.HTTPError:
                print "Http error"
                return None
