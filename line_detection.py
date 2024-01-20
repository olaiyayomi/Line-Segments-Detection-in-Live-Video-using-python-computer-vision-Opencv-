import cv2 as cv
import numpy as np
import sys

video = cv.VideoCapture(0)

if not video.isOpened():
    sys.exit("unable to locate camera")

while True:
    __, frame = video.read()
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    canny = cv.Canny(gray, 50, 150, apertureSize = 3)
    
    line = cv.HoughLinesP(canny, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
    try:
        for lines in line:
            x1,y1,x2,y2 = lines[0]
        
            cv.line(frame, (x1,y1), (x2,y2), 255, 2)
    
            cv.imshow("my video2", frame)
            cv.imshow("my video3", canny)
    
    except TypeError:
        
        continue
            
    key = cv.waitKey(1)
    
    if key == ord("q"):
        break
        
video.release()
cv.destroyAllWindows()
