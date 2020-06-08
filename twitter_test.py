import tweepy
#assign variables to the key,secret and token
consumer_key = "your consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access secret"
#use OAuthHandler to pass the consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#set access token and secret
auth.set_access_token(access_token, access_token_secret)
#intergrate to the api
api = tweepy.API(auth)
#write a tweet to our twitter account
#tweet = "Hello!"
#api.update_status(status=tweet)
tweet2 ="just testing my twitter app set_up!"
api.update_status(status=tweet2)
