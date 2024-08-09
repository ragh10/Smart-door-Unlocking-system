import cv2 
import numpy as np
import os
import time
import sys

if not os.path.exists("faces"):
    os.mkdir("faces")
def detect_face(img,count):
    bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(bw,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        crop_img = frame[y:y+h,x:x+w]
        cv2.imwrite("faces/"+"image"+str(count)+".png",crop_img)
    return img 
count=0
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))

while True:
    ret,frame = cap.read()
    count+=1
    #frame = cv2.addWeighted(frame,2,np.zeros(frame.shape,frame.dtype),0,50)
    canvas = detect_face(frame,count)
    resize = cv2.resize(canvas,(600,480))
    cv2.imshow("Frame",frame)
    if canvas.all() != None:
        break
    if cv2.waitKey(1)=='q':
        break
cap.release() 