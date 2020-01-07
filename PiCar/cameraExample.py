#import picamera and time modules
from picamera import PiCamera
import time

#create new picamera instance called camera
camera = PiCamera()

#flip camera view vertically
camera.vflip = True

#show camera preview onscreen
camera.start_previw()

#wait for 15 seconds before ending the script
time.sleep(15)
