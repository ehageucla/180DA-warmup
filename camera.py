#OPENCV SAMPLE CODE used as a base for this file found at
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

# COLOR SPACE SECTION
# CREDIT: https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
# define range of blue color in HSV (found using GIMP)
# GIMP has an HSV range of 360 degrees and 180 degrees is used by OpenCV
# against dimly lit background a lower value made the camera highly sensitive

# RECTANGLE SECTION
# CREDIT: https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
# create a rectangle around the mask

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([80,30,75])
    upper_blue = np.array([95,230,102])

    # Threshold the HSV image to get only blue colors CREDIT openCV colorspaces
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    x, y, w, h = cv.boundingRect(mask)
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()