import cv2 as cv
import numpy as np

def nothing(x):
	pass

c = cv.VideoCapture(0)
cv.namedWindow('coo')
cv.createTrackbar('lower_h','coo',0,179,nothing)
cv.createTrackbar('lower_s','coo',0,255,nothing)
cv.createTrackbar('lower_v','coo',0,255,nothing)
cv.createTrackbar('upper_h','coo',0,179,nothing)
cv.createTrackbar('upper_s','coo',0,255,nothing)
cv.createTrackbar('upper_v','coo',0,255,nothing)

while True:
	ret,frame = c.read()
	if ret == True:
		hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
		h = cv.getTrackbarPos('lower_h','coo')
		s = cv.getTrackbarPos('lower_s','coo')
		v = cv.getTrackbarPos('lower_v','coo')
		uh = cv.getTrackbarPos('upper_h','coo')
		us = cv.getTrackbarPos('upper_s','coo')
		uv = cv.getTrackbarPos('upper_v','coo')

		lower_val = np.array([h,s,v],np.uint8)
		upper_val = np.array([uh,us,uv],np.uint8)
		mask = cv.inRange(hsv, lower_val, upper_val)
		
		res = cv.bitwise_and(frame,frame, mask = mask)
		
		cv.imshow('coo',frame)
		cv.imshow('mask',mask)
		cv.imshow('cool',res)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
c.release()
cv.destroyAllWindows()
