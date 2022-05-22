import cv2
import numpy as np

# #import image
# img = cv2.imread('Resources/lena.jpg')
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# #import video
# cap = cv2.VideoCapture('Resources/AnimeMix.mp4')
# while True :
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0XFF == ord('q') :
#         break

# #opening web cam
# cap = cv2.VideoCapture(0)
# cap.set(3,640) #width
# cap.set(4,480) #height
# cap.set(10,100) #brightness
# while True :
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(0) & 0XFF == ord('q') :
#         break

# #Converting image to greySale
# img = cv2.imread('Resources/lena.jpg')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grey Image', imgGray)
# cv2.waitKey(0)

#blur grey image
img = cv2.imread('Resources/lena.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
cv2.imshow('Grey Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.waitKey(0)



