EC601-MiniProject1- Twitter & Google VideoIntelligence API
The aim of Miniproject is to build a library (in python) that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video.

1. Use Tweepy to Download Images

1.1 Get the Twitter API Credential:
Go to https://developer.twitter.com/content/developer-twitter/en.html and apply for a Twitter developer account. Then you will get your  own access keys and tokens.

1.2 Install Tweepy：
Type "pip install tweepy" in the terminal.

1.3 Run the project:
Please open the file "Miniproject1.py" and enter your own access keys and tokens in the blank (line 17~20).
Then, enter a Twitter account you are interested in in line 99 and choose how many images you want to collect from tweets in line 47.
At last, type "python Tweepy-images.py" in the terminal.  

2. Use FFMPEG to Convert Images into a Video

Type "pip install ffmpeg" to install ffmpeg. 
Run the "convert_to_video.py" which calls a system command "ffmpeg -f image2 -r 0.2 -i /home/ece-student/Pictures/%02d.jpg "+screen_name+".mp4" to output a mp4. 
Ps: The duration of every image is depends on the number after "-r" so that you can decide the length of your video. 

3.Use Google-Cloud-VideoIntelligence API to analyze Images

3.1 Set up the Google Cloud VideoIntelligence environment:
Go to https://cloud.google.com/video-intelligence/docs/analyze-labels#video_analyze_labels-python and follow the instructions.

3.2 Run the google_analysis.py:
Once you have run the program successfully, you can see that images unloaded by users are downloaded in your file now and the API automatically analyze what the images are about, meanwhile, a wonderful video is presented to you.
