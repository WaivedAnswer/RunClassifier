# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:04:31 2019

@author: quinn.ramsay
"""
import cv2
import datetime

from detectors import PredictionDetector

CV_CAP_PROP_POS_MSEC = 0
CV_CAP_PROP_POS_FRAMES = 1


def get_image_path(relative_path):
    return "images/" + relative_path


def get_video_path(relative_path):
    return "videos/" + relative_path


# load video
video_capture = cv2.VideoCapture(get_video_path("RingRig.mov"))

detector = PredictionDetector()

frames_to_skip = 30
while video_capture.isOpened():
    ret, frame = video_capture.read()
    if not ret:
        break
    # every x frames grab frame image
    currFrameCount = video_capture.get(CV_CAP_PROP_POS_FRAMES)
    if currFrameCount % frames_to_skip == 0:
        # classify image/detect
        obstacle = detector.classify(frame)
        if obstacle is not None:
            milliseconds = video_capture.get(CV_CAP_PROP_POS_MSEC)
            time = datetime.timedelta(milliseconds=milliseconds)

            print(obstacle, time)
            # cv2.imwrite(get_image_path(str(time.total_seconds()) + "_" + obstacle+ ".png"), frame)


        # if it is what we'd like get timestamp and add it to sightings

# gather timestamps into durations
video_capture.release()
