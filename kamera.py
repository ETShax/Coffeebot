import picamera
import datetime
import time
cam = picamera.PiCamera()
cam.resolution = (640, 480)
kuva = "zoomi"+".jpg"
cam.capture(kuva)
