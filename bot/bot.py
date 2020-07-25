import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("klLc4LqNpq1UPXL9SZv7XQNQq", "9kFH9R2ZkteZu64JjDBydDeXvu105xMPvl3K92e0ULKV6K13lP")
auth.set_access_token("1265867141699559425-Fs1xVWUxGdOcN64f7WVopjgPVLO2Ps","00rpl6Tng9tCPPdje4EOKCTIdt5Mo1syij4YVRuV5NUxU")

# Create the API obj
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


'''
# This will print out 20 tweets currently in timeline

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
'''

'''
# This will get the user's info, then last 20 followers' of that user's info
user = api.get_user("jakeesanchezz")
print("User Info:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 followers:")
for follower in user.followers():
    print(follower.name)

'''




'''

# this will follow my actual account
api.create_friendship("jakeesanchezz")

'''




'''

# this will go and search the last 10 tweets in english including query and like it!
for tweet in api.search(q="coral reef", lang="en", rpp=10):
    try:
        api.create_favorite(tweet.id)
    except:
        continue

'''



