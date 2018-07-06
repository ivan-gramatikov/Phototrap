import numpy as np # this line tells Python to import numpy, a library required for computations, which will be made on the image
import cv2 # this line imports the OpenCV library so the programmer can use OpenCV’s libraries in Python
import sys # these both lines basically import modules to aid in argument handling, 
import os # usage of paths, etc. 

cascPath = sys.argv[1] #positional argument to accept the path to the pre-made cascade
face_cascade=cv2.CascadeClassifier(cascPath) #creating the cascade
cap = cv2.VideoCapture(0) # sets the video source to the default webcam (in this case, the CANYON USB webcam  

while 1: #endless loop 
    ret, img = cap.read() # capture the video. The read() function reads one frame from the video source, which in this example is the webcam. This returns:
#1. The actual video frame read (one frame on each loop)
#2. A return code, which will “sound the alarm” if the case was reading from a file and having ran out of frames to read, which cannot happen with a webcam

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts an image from one color space to another given a source, turns from a RGB image to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #searching for a face

    for (x,y,w,h) in faces:  # the whole for cycle is responsible for rectangle creation around the coordinates where the face is located
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img',img) #showing the frames in a simple window
    if faces!=(): #if faces variable is not empty,
     cv2.imwrite('/home/ubuntu/Desktop/imagescamera/x.png', img) #a still image is taken by OpenCV, specifically by the imwrite method and written to a directory in the png format by the name x. Since this project is merely to serve as a basis, it only captures the last seen face or faces. 
     
    k = cv2.waitKey(30) & 0xff #if a key is pressed, the program stops. It can also be stopped by pressing Ctrl+C or Ctrl+Z, which produces an interrupt by the user
    if k == 27:
        break

cap.release() #releasing the capture 
cv2.destroyAllWindows() # stopping the window, which shows the frames and quits the program
