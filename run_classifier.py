# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:04:31 2019

@author: quinn.ramsay
"""
import datetime

from detectors import PredictionDetector
from video_analysis import VideoAnalyzer


def get_image_path(relative_path):
    return "images/" + relative_path


def get_video_path(relative_path):
    return "videos/" + relative_path


detector = PredictionDetector()
analyzer = VideoAnalyzer(detector)

event_list = analyzer.analyze_video(get_video_path("RingRig.mov"))

for event in event_list:
    name = event[0]
    time_in_milliseconds = event[1]
    time = datetime.timedelta(milliseconds=time_in_milliseconds)
    print(name, time)
# gather timestamps into durations
