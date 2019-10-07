import datetime

import cv2


class VideoAnalyzer:
    CV_CAP_PROP_POS_MSEC = 0
    CV_CAP_PROP_POS_FRAMES = 1

    def __init__(self, detector, frames_to_skip=30):
        # load video
        self.detector = detector
        self.frames_to_skip = frames_to_skip

    def analyze_video(self, file_path):
        event_list = []
        video_capture = cv2.VideoCapture(file_path)

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if not ret:
                break

            if self._should_analyze_frame(video_capture):
                obstacle = self.detector.classify(frame)
                if obstacle is not None:
                    milliseconds = video_capture.get(self.CV_CAP_PROP_POS_MSEC)
                    event_list.append((obstacle, milliseconds))

        video_capture.release()
        return event_list

    def _should_analyze_frame(self, video_capture):
        curr_frame_count = video_capture.get(self.CV_CAP_PROP_POS_FRAMES)
        should_analyze = curr_frame_count % self.frames_to_skip == 0
        return should_analyze
