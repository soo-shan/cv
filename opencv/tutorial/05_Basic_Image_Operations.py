import cv2
import numpy as np

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

# using array.items, array.itemsets methods for single pixel access
# accessing blue pixel
red = img.items()

print('blue pixel value at 100,100: ',blue)


