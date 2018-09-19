import sys
import os

def convert(screen_name):
    os.system("ffmpeg -f image2 -r 0.2 -i /home/ece-student/Pictures/%02d.jpg "+screen_name+".mp4")
