from picamera import PiCamera
from os import system
import datetime
from time import sleep

tlminutes = 0.5 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 0.25 #number of seconds delay between each photo taken
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take
print("number of photos to take = ", numphotos)

fps = 12 #frames per second timelapse video

dateraw = datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (1024, 768)
camera.vflip = True
camera.color_effects = (128,128) #turn camera to black&white


system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start

for i in range(numphotos):
    camera.capture('/home/pi/Pictures/image{0:06d}.jpg'.format(i))
    camera.color_effects = (128,128) #turn camera to black&white
    sleep(secondsinterval)
print("Done taking photos.")
print("Please standby as your timelapse video is created.")

system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p ./Video/memory-{}.mp4'.format(fps, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
print('Timelapse video is complete. Video saved as ./Video/memory-{}.mp4'.format(datetimeformat))