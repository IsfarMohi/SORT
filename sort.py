import numpy as np
from collections import defaultdict

class Sort:
    def __init__(self):
        self.trackers = defaultdict(dict)
        self.next_id = 0

    def update(self, detections):
        new_tracks = []
        for det in detections:
            x, y, w, h = det[:4]
            track_id = self.next_id
            self.trackers[track_id] = {'bbox': [x, y, w, h]}
            new_tracks.append([x, y, w, h, track_id])
            self.next_id += 1
        return new_tracks
