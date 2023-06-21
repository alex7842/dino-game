import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto


c=cv2.VideoCapture(0)
hd=HandDetector(maxHands=1)
while 1:
    rt,frame=c.read()
    frame=cv2.resize(frame,(900,600))
    cvzone.putTextRect(frame,"START",[360,40],scale=3,thickness=2,border=2)
    hand,frame=hd.findHands(frame)
    if hand:
        hands=hand[0]
        lmlist=hands['lmList']
       # print(lmlist[4])
        length,info,frame=hd.findDistance(lmlist[4][0:2],lmlist[8][0:2],frame)
        length=round(length)
        if length<50:
            auto.press('up')
    cv2.imshow('frame',frame)
    cv2.waitKey(1)