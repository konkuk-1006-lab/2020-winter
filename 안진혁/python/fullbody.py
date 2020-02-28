import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = "people_full.jpg"

image1 = cv2.imread('./Image/'+filename)
grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier('./Image/haarcascade_fullbody.xml')

body = body_cascade.detectMultiScale(grayImage1, 1.01, 25, minSize=(30, 30))

for (x,y,w,h) in body :
    cv2.rectangle(image1,(x,y),(x+w,y+h),(0,0,255),3)

plt.subplot(1, 3, 1)
plt.imshow(image1, cmap='gray')

plt.show()
