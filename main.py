import cv2
import pandas as pd
from ultralytics import YOLO
from sort import Sort
import cvzone
import numpy as np

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('p.mp4')

with open("coco.txt", "r") as my_file:
    class_list = my_file.read().strip().split("\n")

tracker = Sort()

area1 = [(494, 289), (505, 499), (578, 496), (530, 292)]
area2 = [(548, 290), (600, 496), (637, 493), (574, 288)]

while True:    
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1020, 500))

    results = model.predict(frame)
    a = results[0].boxes.data.cpu().numpy()

    detections = []
    for row in a:
        x1, y1, x2, y2, conf, cls_id = map(int, row[:6])
        class_name = class_list[cls_id]
        if class_name == 'person':
            detections.append([x1, y1, x2 - x1, y2 - y1, conf])  # Adding confidence as needed

    tracks = tracker.update(np.array(detections))

    for track in tracks:
        x1, y1, x2, y2, track_id = map(int, track)
        cv2.rectangle(frame, (x1, y1), (x1 + x2, y1 + y2), (255, 255, 255), 2)
        cvzone.putTextRect(frame, f"Person {track_id}", (x1, y1), 1, 1)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
