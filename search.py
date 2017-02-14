#!/usr/bin/python
#################################################
#	 this program uses the python library Twython(created by twitter)
# 	to search(with the search function) the hashtag JohnQuincyAdams 
# 	and then displays  the top 5 results(count = 5)
#
#################################################
from twython import Twython, TwythonError


t =  Twython(APP_KEY, APP_SECRET)

results = t.search(q = "#JohnQuincyAdams", count = 5)

all_tweets = results['statuses']

for tweet in all_tweets:
    print(tweet['text'])