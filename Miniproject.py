#!/usr/bin/env python
# encoding: utf-8
#Author - Lekai Song

#code with "##" is what author have tried but failed.

import tweepy
import os
import urllib
import io
import argparse
from google.cloud import videointelligence
##import wget
##from bs4 import BeautifulSoup

consumer_key = "TbOHFkGD6O6MkZmUwZaEJeFvS"
consumer_secret = "g1wbA7SHlPXvKJASVnagWYHQYb3pC47smsIDkfeVX63OVHlMMS"
access_key = "1038159139044614144-ux2em514t7bsDWRtjUm06LztrK090M"
access_secret = "36ZjqZh8TeOGuzU7U1jpsmKZ5aOYew3QDKQYxuiTYechB"

cwd=os.getcwd()
print(cwd)

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
        urllib.request.urlretrieve(url, cwd + '/%02d.jpg'%i)
        i += 1
    ##for url in tweetsmedia:
        ##wget.download -c 'url' -O 'image%d'%i

#image duration depends on -r
def convert(screen_name):
    os.system("ffmpeg -f image2 -r 0.5 -i './%02d.jpg' "+screen_name+".mp4")
    
#must pip install google-cloud-videointelligence
def google():
    #https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.getcwd()+'/google.json'
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(os.path.join(cwd,""+screen_name+".mp4"),'rb')as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(features=features, input_content=input_content)
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    print('\nFinished processing.')

    # Process video/segment level label annotations
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print('Video label description: {}'.format(segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print('\tLabel category description: {}'.format(category_entity.description))

        #show the matching degree
        for i, segment in enumerate(segment_label.segments):
            confidence = segment.confidence
            print('\tConfidence: {}'.format(confidence))
            print('\n')

if __name__ == '__main__':
    screen_name = args["user"]
    get_all_tweets(screen_name)
    convert(screen_name)
    google()
