import tweepy
#assign variables to the key,secret and token
consumer_key = "dyrc7limtw0FCZoopEvorU5tC"
consumer_secret = "1HG5gKbSCapWguP2XTXfgYbNEfAvU4WipMUKuGRslTwY73RkXI"
access_token = "1245685147946700801-xaHmExMgRGrwraIRVgLoLGbt96NAMF"
access_token_secret = "Z0zrGILGQFhClma6bnFe6OMNubtALLfBKB7ulhm1eM7TB"
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
