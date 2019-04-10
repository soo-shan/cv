import numpy as np
import cv2

# # some common arguments as given below:

# #         img : The image where you want to draw the shapes
# #         color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
# #         thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
# #         lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.

# create a black image
black_img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('title', black_img)
cv2.waitKey(0)

# draw a diagonal blue line with thickness of 5px
diag_line = cv2.line(img=black_img,
                     pt1=(0, 0),
                     pt2=(511, 511),
                     color=(255, 0, 0),
                     thickness=5)
cv2.imshow('title', diag_line)
cv2.waitKey(0)

# draw rectangle
rect_img = cv2.rectangle(img=black_img,
                         pt1=(384, 0),
                         pt2=(510, 128),
                         color=(0, 255, 0),
                         thickness=3)
cv2.imshow('title', rect_img)
cv2.waitKey(0)

# drawing circle
circle_img = cv2.circle(img=diag_line,
                        center=(447, 63),
                        radius=63,
                        color=(0, 0, 255),
                        thickness=-1)
cv2.imshow('title', circle_img)
cv2.waitKey(0)

# draw Ellipse
black_img = np.zeros((512, 512, 3), np.uint8)
ellipse_image = cv2.ellipse(img=black_img,
                            center=(256, 256),
                            axes=(100, 50),
                            angle=0,
                            startAngle=0,
                            endAngle=180,
                            color=(0, 0, 255),
                            thickness=-1)
cv2.imshow('title', ellipse_image)
cv2.waitKey(0)

# draw Polygon
pts = np.array([[10, 5], 
                [20, 30], 
                [70, 20], 
                [50, 10]], np.int32)
pts =pts.reshape((-1,1,2))
black_img = np.zeros((512, 512, 3), np.uint8)
polygon_img =cv2.polylines(black_img,pts=[pts],isClosed=True,color=(0,255,255))
cv2.imshow('title',polygon_img)
cv2.waitKey(0)

# Adding text to images
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('../data/random/0002.jpeg')
# img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, text = 'Hello There',org = (45,30), 
            fontFace = font, fontScale = 1,
            color = (160,255,122),thickness = 2, lineType =cv2.LINE_AA)
cv2.imshow('title',img)
cv2.waitKey(0)