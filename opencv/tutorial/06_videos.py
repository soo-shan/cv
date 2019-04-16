import cv2
import numpy as np

cap = cv2.VideoCapture('../data/vending_machine.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
