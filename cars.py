


import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image

count = 0
c = 0
faceCascade = cv2.CascadeClassifier('/home/ns/anaconda3/share/OpenCV/haarcascades/cars.xml')





video_capture = cv2.VideoCapture(0)




while (c != 100):
    # Capture frame-by-frame
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=2);
	    
	print(faces)
	    #crop1 = gray.crop(faces)

	    #crop1.show()
	    # Draw a rectangle around the faces
	for (x, y, w, h) in faces:
	        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	        #area1 = (x, y, w, h)
	        crop1 = frame[y:y+h, x:x+w]
	        #cv2.imwrite("frame%d.jpg" % count, crop1)     # save frame as JPEG file      
	        print('Read a new frame: ', ret)
	        count = count + 1
	        cv2.imshow('frames: ',frame)

	c = c + 1


	    #if cv2.waitKey(1) & 0xFF == ord('q'):
	    #    break


video_capture.release()
cv2.destroyAllWindows()
print(count/c)