import numpy as np
import cv2 as cv

cap = cv.VideoCapture('challenge.mp4')
#cap = cv.VideoCapture(0)

# take first frame of video
ret, frame = cap.read()
# setup initial position of window
x, y, width, height = 830, 400, 100, 50
trackWindow = (x, y, width, height)
# set up Region Of Interest for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# set up termination criteria, either 10 iteration or move by at least 1 pt.
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('roi', roi)


while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, trackWindow = cv.CamShift(dst, trackWindow, term_crit)

        pts = cv.boxPoints(ret)
        pts = np.int0(pts)  # convert values to integers
        finalImage = cv.polylines(frame, [pts], True, (255, 0, 0), 3)
        # x, y, w, h = trackWindow
        # finalImage = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        cv.imshow('dst', dst)
        cv.imshow('Final Image', finalImage)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cv.destroyAllWindows()
cap.release()