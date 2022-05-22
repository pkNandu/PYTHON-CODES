import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[200:300, 100:200] = 255,0,0

# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255,0,0), 3) #line
# cv2.rectangle(img, (100, 100), (200,300), (255, 255, 0), cv2.FILLED) #rectangle\
# cv2.circle(img, (300,300), 30, (0, 0, 255), 3) #circle
cv2.putText(img, 'helloNANDU', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1) #text
cv2.putText(img, 'helloNANDU', (200, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 150, 0), 1) #text
cv2.putText(img, 'helloNANDU', (300, 250), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 150, 0), 1) #text
cv2.putText(img, 'helloNANDU', (400, 350), cv2.FONT_HERSHEY_COMPLEX, 4, (0, 150, 0), 1) #text


cv2.imshow('image', img)

cv2.waitKey(0)