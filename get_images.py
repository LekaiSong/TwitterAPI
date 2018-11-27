#!/usr/bin/env python
import tweepy
import os
import urllib
import argparse
##import wget
##from bs4 import BeautifulSoup

consumer_key = "TbOHFkGD6O6MkZmUwZaEJeFvS"
consumer_secret = "g1wbA7SHlPXvKJASVnagWYHQYb3pC47smsIDkfeVX63OVHlMMS"
access_key = "1038159139044614144-ux2em514t7bsDWRtjUm06LztrK090M"
access_secret = "36ZjqZh8TeOGuzU7U1jpsmKZ5aOYew3QDKQYxuiTYechB"

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="user you're interested in")
ap.add_argument("-i", "--images", required=True, help="amount of images you want to download")
args = vars(ap.parse_args())

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
        if(len(alltweets) > int(args["images"])):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))

    tweetsmedia = set()
    for status in alltweets:
        media = status.entities.get('media',[])
        if (len(media)>0):
            tweetsmedia.add(media[0]['media_url'])
    
    #download images named 01~25
    i=0
    for url in tweetsmedia:
        print(url)
        urllib.request.urlretrieve(url, os.getcwd()+'/%02d.jpg'%i)
        i += 1
    ##for url in tweetsmedia:
        ##wget.download -c 'url' -O 'image%d'%i
