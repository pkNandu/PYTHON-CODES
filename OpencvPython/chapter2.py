import cv2
import numpy as np

#edge detection in image using Canny, image dilation, image Erotion
img = cv2.imread('Resources/lena.jpg')
kernel = np.ones((5,5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #image grey scaling
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  #image blurring
imgCanny = cv2.Canny(img, 150, 200) #edge detectionQQQ
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1) #dilation
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1) #erotion
cv2.imshow('Grey Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)