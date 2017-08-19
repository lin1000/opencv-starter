import argparse
import cv2
import time
import sys
from pathlib import Path
import os
import common.fileutil
import re

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-i", "--image", required=False, help="Path to the image(no default)")
group.add_argument("-p", "--path", required=False, help="Path to the image folder")
parser.add_argument("-w", "--window", type=int, default=800, help="window size (default:%(default).1d)")
parser.add_argument("-s", "--stepsize", type=int, default=80, help="step size for stride(default:%(default).1d)" )
parser.add_argument("-o", "--outputpath", type=str, default="images_output", help="output fold (er path of the sliding images(default:%(default)s)")
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


def sliding_window_save(image, stepsize, winW, winH,filename):
    print(filename)
    # loop over the sliding window for each layer of the pyramid
    for (x, y, window) in sliding_window(image, stepSize=stepsize, windowSize=(winW, winH)):
        # if the window does not meet our desired window size, ignore it
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        
        roi = window.copy()
        #cv2.imshow("Window", roi)
        cv2.imwrite("{path_to_ouput_image}-{x}-{y}{ext}".format(path_to_ouput_image=os.path.join(path_to_ouput_image,os.path.splitext(filename)[0]), x=x, y=y, ext=os.path.splitext(filename)[1]),roi)
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

# set the variables
(winW, winH) = (args["window"], args["window"])
stepsize = args["stepsize"]

if(args["path"] is not None):
    path_to_input_image = args["path"]
    path_to_input_image_to_be_check = Path(path_to_input_image)
    if path_to_input_image_to_be_check.is_dir():
        pass
    else :
        print("{path_to_input_image} is not a directory".format(path_to_input_image=path_to_input_image))
        parser.print_help()
        sys.exit(1)

if(args["image"] is not None):
    file_to_input_image = args["image"]
    file_to_input_image_to_be_check = Path(file_to_input_image)
    if file_to_input_image_to_be_check.is_file():
        pass
    else :
        print("{file_to_input_image_to_be_check} is not a directory".format(file_to_input_image_to_be_check=file_to_input_image_to_be_check))
        parser.print_help()
        sys.exit(1)

path_to_ouput_image = args["outputpath"]
path_to_ouput_image_to_be_check = Path(path_to_ouput_image)
if path_to_ouput_image_to_be_check.is_dir():
    pass
else :
    print("{path_to_ouput_image} is not a directory".format(path_to_ouput_image=path_to_ouput_image))
    parser.print_help()
    sys.exit(1)

if(args["image"] is not None):
    print(file_to_input_image)
    files = [file_to_input_image]
elif(args["path"] is not None):
    files = common.fileutil.listAllFiles(path_to_input_image)

files_img = list(map(lambda x: [x,cv2.imread(x)],files))
print(files_img)
list(map(lambda x: sliding_window_save(x[1], stepsize, winW, winH, os.path.basename(x[0])), files_img))