import os
from time import time, sleep
from windowcapture import WindowCapture

# Change the working directory to the folder this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Counter-Strike')

loop_time = time()
while(True):

    # get an updated image of the game
    wincap.get_screenshot()

    #two screenshots by second
    sleep(0.5)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
