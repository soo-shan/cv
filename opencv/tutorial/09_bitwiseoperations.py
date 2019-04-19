import numpy as np
import cv2

img1 = cv2.imread('data/messi5.jpg')
img2 = cv2.imread('data/opencv-logo-white.png')

cv2.imshow('img1',img1)
cv2.waitKey(0)

cv2.imshow('logo',img2)
cv2.waitKey(0)

# create roi
rows,cols,channels = img2.shape
roi = img1[25:rows+25, 150:cols+150 ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('mask',mask)
cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('inv_mask',mask_inv)
cv2.waitKey(0)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.waitKey(0)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2_fg',img2_fg)
cv2.waitKey(0)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
# slicing changes original array
roi[:,:] = dst


cv2.imshow('final',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

