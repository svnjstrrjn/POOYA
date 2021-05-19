from os import system
from time import sleep

while True:
    system('python ./AudioRecording.py & python ./TimelapseRecording.py')
    sleep(300)
