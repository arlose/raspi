# camera_test.py
import os
from bypy import ByPy
import picamera
import time
import datetime
# Create camera interface
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 30
camera.vflip = True
bp=ByPy()
newestfile="newest.jpg"
while True:
	filename = time.strftime("%Y_%m_%d_%H_%M_%S.jpg", time.localtime())
	camera.capture(filename)
	#camera.capture(newestfile)
	#os.copy(filename,newestfile)
	i = datetime.datetime.now()
	hour = i.hour
	sleeptime = 600
	if hour > 22 or hour < 5:
		sleeptime = 3000
	bp.upload(filename, 'home/')
	bp.upload(filename, newestfile)
	os.remove(filename)
	time.sleep(sleeptime)
    
    
