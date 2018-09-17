# Twitter-API
#!/usr/bin/env python
# encoding: utf-8
#Author - Lekai Song


import tweepy
import json
import urllib
from bs4 import BeautifulSoup

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
       
    file = open('tweet.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    print("Done")
    file.close()

def get_image(info):
	soup = BeautifulSoup(info,'html.parser')
	all_image = soup.find_all('img',class_ = "BDE_Image")
	x=1
	for image in all_image:
		print(all_image)
		urllib.request.urlretrieve(image['scr'],"/home/ece-student/Pictures/%s.jpg"%(x))
		x = x+1

if __name__ == '__main__':
    info = get_all_tweets("@Apple")
    get_image(info)
