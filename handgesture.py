import cv2
from cvzone.HandTrackingModule import HandDetector

detector=HandDetector(maxHands=2,detectionCon=0.8)

img=cv2.VideoCapture(0)
while True:
    cap,frame=img.read()
    hand,image=detector.findHands(frame)
    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
