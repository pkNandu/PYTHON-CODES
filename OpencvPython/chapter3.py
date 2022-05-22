import cv2

img = cv2.imread('Resources/lena.jpg')
print(img.shape)
#Resize image
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)
#crop image
imgCrop = img[0:200, 200:500]
cv2.imshow('Image', img)
cv2.imshow('Resized Image', imgResize)
cv2.imshow('Croppped Image', imgCrop)
cv2.waitKey(0)