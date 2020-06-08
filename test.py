import tweepy
#create variables for your token, key and secrets
consumer_key = "use your api key value here"
consumer_secret = "use your api secret value  here"
access_token = "paste your access token value here"
access_token_secret = "paste your access_token_secret here"

#use OAuthHandler to pass the consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#set the access token and secret
auth.set_access_token(access_token, access_token_secret)
#integrate with the api
api = tweepy.API(auth)
#push a tweet
tweet = "my very first app intergrated with twitter"
api.update_status(status = tweet)

