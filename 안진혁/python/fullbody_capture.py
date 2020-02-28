import numpy as np
import cv2
from matplotlib import pyplot as plt

filepath = './Image/people_full.mp4'

movie = cv2.VideoCapture(filepath)

if movie.isOpened() == False:
    print ('Can\'t open the File' + (FilePath))
    exit()

cv2.namedWindow('Body')

body_cascade = cv2.CascadeClassifier('./Image/haarcascade_frontalface_default.xml')

while(True):
    ret, frame = movie.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    body = body_cascade.detectMultiScale(grayframe, 1.01, 25, minSize=(30, 30))

    for (x,y,w,h) in body :
        cv2.rectangle(image1,(x,y),(x+w,y+h),(0,0,255),3)
    plt.subplot(1, 3, 1)
    plt.imshow(image1, cmap='gray')

    if cv2.waitKey(33) > 0: break

movie.release()
cv2.destroyWindow('Body')
