import tweepy
import time

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Get this key from Twitter Api u can search u get the api as a Twitter Developer
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# This is the u check if u go over the Rate Limit of Twitters API
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
            time.sleep(1000)

#Keyword u search for
search_string = "python"

# How many tweets u want to like etc.
number_of_tweets = 2

# Search from search string and like th number amount of tweets set in number_of_tweets
for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print("The Tweet has been liked")
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break


#Follow Back Bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == "FOLLOWER NAME":
        follower.follow()
        print("Person has been followed")
        break

# Shows each followers of yours by name
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)

# This is for the twitter timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print (user.name) # Prints UserName
print (user.followers_count) # Prints Follow Count
