import cv2
import picamera
import numpy as np
import argparse



img = cv2.imread('kahvi.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,50,255,0)
im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
a = 0
ar = (0, a)
for cont in contours:
	
	cnt = cont
	area = cv2.contourArea(cnt)
	if area > ar[0]:
		ar = (area, a)
	#output= cv2.drawContours(img,[cnt], 0,(0,255,0),3)
	#cv2.imshow("images%s"%a, output)
	#cv2.waitKey()
	a+=1
	
print ar
output= cv2.drawContours(img,contours, ar[1],(0,255,0),3)
cv2.imshow("images%s"%a, output)
cv2.waitKey()	
cnt = contours[0]
area = cv2.contourArea(cnt)
M = cv2.moments(cnt)


#cv2.imshow("images", output)
cv2.waitKey()
