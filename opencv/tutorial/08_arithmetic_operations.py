import numpy as np
import cv2

# Image addition
# OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

x = np.uint8([250])
y = np.uint8([10])
print('opencv addition of 250,10: ',cv2.add(x,y)) # 250+10 = 260 => 255
print('numpy addition of 250,10: ', x+y)          # 250+10 = 260 % 256 = 4

# image blending
img1 = cv2.imread('random/0003.jpeg')

cv2.imshow('image',img1)
cv2.waitKey(0)

img2 = cv2.flip(img1,0)
# print(min(img1.shape,img2.shape))

def image_blend(value):
    alpha =  value/100
    beta = 1 - alpha
    gamma = 0 
    dst = cv2.addWeighted(img1,alpha,img2,beta,gamma)
    cv2.imshow('image', dst)
    print(value)
    

cv2.namedWindow('image')
trackbar_title = 'alpha * 100'
cv2.createTrackbar(trackbar_title, 'image', 0, 100, image_blend)

cv2.waitKey(0)