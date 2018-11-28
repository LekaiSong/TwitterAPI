EC601-MiniProject1
==================
Twitter & Google VideoIntelligence APIs
---------------------------------------

### 1. Goal
### To build a library (in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.

>#### 1) Use Tweepy to Download Images

>#### 2) Use FFMPEG to Convert Images into a Video

>#### 3) Use Google-Cloud-VideoIntelligence API to analyze Images

### 2. Environment Preparation
>#### 1) Get the Twitter API Credential:
>>#### Go to https://developer.twitter.com/content/developer-twitter/en.html and apply for a Twitter developer account. Then you will get your own access keys and tokens.

>#### 2) Set up the Google Cloud VideoIntelligence environment:
>>#### Go to https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python and follow the instructions.

>#### 3) Install Tweepy & FFMPEG:
>>#### Type "pip install tweepy" in the terminal.
>>#### Type "pip install ffmpeg" to install ffmpeg. 

>#### 4) Run the project:
>>#### 'python Miniproject1.py -u @UserYouAreInterestedIn -i AmountOfImagesToDownload'. <br> The output file named @UserYouAreInterestedIn.mp4 is stored in the current path.
>>#### eg. 'python Miniproject1.py -u @maroon5 -i 100'
>>![screenshot](http://github.com/LekaiSong/Twitter-API/raw/master/maroon5_terminal_screenshot.png)

#### Once you have run the program successfully, you can see that images unloaded by users are downloaded in your file now and the API automatically analyze what the images are about. Meanwhile, a wonderful video is presented to you.
