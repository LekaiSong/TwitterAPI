#!/usr/bin/env python
import os

#image duration depends on -r
def convert_to_video(screen_name):
    os.system("ffmpeg -f image2 -r 0.5 -i './%02d.jpg' "+screen_name+".mp4")
