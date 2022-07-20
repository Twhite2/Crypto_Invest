import os
import tweepy as tw
import pandas as pd

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = crypto_coin
date_since = age

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

[tweet.text for tweet in tweets]

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs
