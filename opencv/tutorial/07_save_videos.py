import numpy as np
import cv2

cap = cv2.VideoCapture('../data/vending_machine.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('../data/vending_machine_output.mp4',fourcc, 15, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        # flip the image vertically
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()