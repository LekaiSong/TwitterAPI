# Twitter-API
#!/usr/bin/env python
# encoding: utf-8
#Author - Lekai Song


import tweepy
import json
import wget
#import urllib
#from bs4 import BeautifulSoup

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
        
    alltweets = []    
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    #.append different?
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))

    tweetsmedia = set()
    for status in alltweets:
        media = status.entities.get('media',[])
        if (len(media)>0):
            tweetsmedia.add(media[0]['media_url'])
    
    #i=1
    for url in tweetsmedia:
        wget.download(url) #-O /home/ece-student/pictures/image%d.jpg %i
        #i += 1
        pass   

if __name__ == '__main__':
    get_all_tweets("@maroon5")
    
