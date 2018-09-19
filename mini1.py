#!/usr/bin/env python
# encoding: utf-8
#Author - Lekai Song


import tweepy
import os
import urllib
from urllib import request

import sys
import io
import argparse
from google.cloud import videointelligence
#import wget
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
        if(len(alltweets) > 25):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))

    tweetsmedia = set()
    for status in alltweets:
        media = status.entities.get('media',[])
        if (len(media)>0):
            tweetsmedia.add(media[0]['media_url'])
    
    i=0
    for url in tweetsmedia:
        #print(url)
        urllib.request.urlretrieve(url,'/home/ece-student/Pictures/%02d.jpg'%i)
        i += 1
    #for url in tweetsmedia:
        #wget.download -c 'url' -O 'image%d'%i


def convert(screen_name):
    os.system("ffmpeg -f image2 -r 0.2 -i /home/ece-student/Pictures/%02d.jpg "+screen_name+".mp4")
    

def google(screen_name):
    #https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(path,'rb')as movie:
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

        for i, segment in enumerate(segment_label.segments):
            confidence = segment.confidence
            print('\tConfidence: {}'.format(confidence))
            print('\n')

if __name__ == '__main__':
    screen_name = "@maroon5"
    get_all_tweets(screen_name)
    convert(screen_name)
    google(screen_name)
