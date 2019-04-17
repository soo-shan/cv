import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an Image
img = cv2.imread('random/0004.jpeg')

# image dimentions
print('image dimensions: ',img.shape)

# accessing pixels
px = img[100,100]
print('pixel values at 100,100: ',px)

# accessing blue pixel
blue = img[100,100,0]
print('blue pixel value at 100,100: ',blue)

# using array.item, array.itemset methods for single pixel access
# accessing blue pixel
red = img.item(100,100,2)
print('red pixel value at 100,100: ',red)

# modifying RED value
img.itemset((100,100,2),89)
red = img.item(100,100,2)
print('modified red pixel vaue at 100,100: ', red)

# total number of pixels
print('total number of pixels: ',img.size)

#  Image ROI 
rocket = img[25:55,175:185]

img[25:55, 100:110] = rocket
# # find rocket using bounding box
# rocket_bound = cv2.rectangle(img=img,
#                          pt1=(175, 25),
#                          pt2=(185, 55),
#                          color=(0, 255, 0),
#                          thickness=1)
cv2.imshow('image',img)
cv2.waitKey(0)

# splitting  and merging image image channels
b,g,r = cv2.split(img)
# alternate
# b = img[...,0 ]
cv2.imshow('image',b)
cv2.waitKey(0)

img_merged = cv2.merge((b,g,r))
cv2.imshow('image',img_merged)
cv2.waitKey(0)

# convert all red pixels to zero
img[...,2] = 0
cv2.imshow('image',img)
cv2.waitKey(0)


# # Making borders for images: padding
# # cv2.copyMakeBorder() function takes following arguments
# # src - input image
# # top, bottom, left, right - border width in number of pixels in corresponding directions
# # borderType - Flag defining what kind of border to be added. It can be following types:
# #         cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
# #         cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
# #         cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
# #         cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
# #         cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg

BLUE = [255,0,0]

img1 = cv2.imread('random/0004.jpeg')


replicate = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_CONSTANT,value=BLUE)


plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()



