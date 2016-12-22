import cv2
import picamera
import numpy as np
import os
from PIL import Image
cam = picamera.PiCamera()
cam.resolution = (640, 480)
kuva = "kahvia"+".jpg"
cam.capture(kuva)
img = cv2.imread('kahvia.jpg')
os.system('rm kahvia.jpg')
mustakahvi = [0,0,0]
laihakahvi = [22,7,4]
tosilaiha  = [95,32,40]
tosiharmaa = [57,57,57]
kahvi = [255,255,255]

lower = np.array(mustakahvi, dtype="uint8")
upper = np.array(tosilaiha, dtype="uint8")


mask = cv2.inRange(img,lower,upper)
cv2.imwrite("maskarpone.png",mask)

im = np.asarray(Image.open("maskarpone.png").convert('L'))
im = 1 * (im<127)
m,n = im.shape
asd = (float)(m*n)



output=cv2.bitwise_and(img,img,mask = mask)
#cv2.imshow("images", mask)
#cv2.waitKey()
im = Image.open('maskarpone.png')
os.system('rm maskarpone.png')
pixels = im.getdata()          # get the pixels as a flattened sequence
black_thresh = 255
nblack = 0
for pixel in pixels:
    if pixel < black_thresh:
        nblack += 1
n = len(pixels)/1000-200
nblack = nblack/1000-200
#print (nblack, n, nblack / float(n))
tulos = open("kahvitulos.txt",'w')
x = nblack / float(n)
tulos.write("Pannussa: ")
if x < 0.33:
	tulos.write("Paljon kahvia")
elif 0.33 < x < 0.666:
	tulos.write("Jonkinverran kahvia")
else:
	tulos.write("ei kahvia")
tulos.close()
