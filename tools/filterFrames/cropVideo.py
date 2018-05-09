import numpy as np
import cv2
 

croptop = 520
cropbottom = 250
crop = croptop + cropbottom

width = 1920
height = 1080 - crop

cap = cv2.VideoCapture("camcorder-left/ussi1.mpeg")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 60.0, (width,height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        frame = frame[croptop:(1080 - cropbottom), 0:1920]

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
