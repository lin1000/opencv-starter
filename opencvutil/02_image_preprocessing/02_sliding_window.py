#http://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/

import argparse
import cv2
import time
import sys

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Path to the image(no default)")
parser.add_argument("-w", "--window", type=int, default=128, help="window size (default:%(default).1d)")
parser.add_argument("-s", "--stepsize", type=int, default=8, help="step size for stride(default:%(default).1d)")
args = vars(parser.parse_args())

if( len( args ) == 0):
    parser.print_help()
    sys.exit(1)

def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

# load the image
image = cv2.imread(args["image"])
(winW, winH) = (args["window"], args["window"])
stepsize = args["stepsize"]

# loop over the sliding window for each layer of the pyramid
for (x, y, window) in sliding_window(image, stepSize=stepsize, windowSize=(winW, winH)):
    # if the window does not meet our desired window size, ignore it
    if window.shape[0] != winH or window.shape[1] != winW:
        continue

    # THIS IS WHERE YOU WOULD PROCESS YOUR WINDOW, SUCH AS APPLYING A
    # MACHINE LEARNING CLASSIFIER TO CLASSIFY THE CONTENTS OF THE
    # WINDOW

    window = window.copy()
    cv2.imshow("Window", window)
    # since we do not have a classifier, we'll just draw the window
    #clone = image.copy()
    #cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
    #cv2.imshow("Window", clone)
    
    k = cv2.waitKey(1)
    if k==27:    # Esc key to stop
        sys.exit(0)
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    elif k==112:
        #press p to puase
        while True:
            c = cv2.waitKey(1)
            #press p again to resume
            if(c==112):
                break
            else:
                pass
    #time.sleep(0.0025)