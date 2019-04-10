import numpy as np
import cv2 

# events = [i for i in dir(cv2) if 'EVENT' in i]

# mouse callback function
def draw_circle(event, x, y ,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    '''Explaination of below:
    https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1'''

    if cv2.waitKey(20) & 0xFF == 27: # esc key
        key = cv2.waitKey(20)
        print(key)
        print(cv2.waitKey(20) & 0xFF)
        break
cv2.destroyAllWindows()

