import numpy as np

import cv2
from PIL import Image, ImageChops, ImageOps
import matplotlib.pyplot as plt

from os.path import isfile, join
from os import listdir


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((10,10)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 0.007, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def crop_image1(image):
    im = Image.open(image)
    new_im = trim(im)
    new_im=ImageOps.expand(new_im,border=(15,15,15,15),fill='white')
    return new_im

# mouse callback functionq
def crop(event,x, y,flags,param):
    img = cv2.imread(join(mypath,param))
    cv2.imshow('image',img)
    for i in onlyfiles:
        print(i)
        if event == cv2.EVENT_LBUTTONDBLCLK:
            print(cv2.EVENT_LBUTTONDBLCLK)
            cropped = crop_image1(join(mypath,i))
            cropped = np.array(cropped)
            cropped = cropped[...,::-1]
            cv2.imshow('image',cropped)

# img = np.zeros((512,512,3), np.uint8)
mypath = 'random'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
cv2.namedWindow('image')

cv2.setMouseCallback('image',crop,param=i)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    break    
