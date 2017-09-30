import argparse
import cv2
import numpy as np


"""
python -m opencvutil.01_opencv_basic.07_opencv_classify_color_space -i ./images/mac/mac-01.jpg
"""

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])

image_g = image[:,:,0] #channel from 3->1
image_r = image[:,:,1] #channel from 3->1
image_b = image[:,:,2] #channel from 3->1
if(np.all(image_g==image_r) and np.all(image_g==image_b)):
    print("This is a Grayscaled Image")
else:
    print("This is a BRG Image")