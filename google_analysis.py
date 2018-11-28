#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import io
from google.cloud import videointelligence

#must pip install google-cloud-videointelligence
def google_analysis():
    #https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.getcwd()+'/google.json'
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(os.path.join(os.getcwd(),""+screen_name+".mp4"),'rb')as movie:
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
