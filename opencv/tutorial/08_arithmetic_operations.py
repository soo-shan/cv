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
img2 = cv2.imread('random/0004.jpeg')
print(min(img1.shape,img2.shape))
img1 = img1[:183,:150]
img2 = img2[:150,:150]

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

