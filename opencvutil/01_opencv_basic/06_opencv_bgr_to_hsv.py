import cv2
import numpy as np

"""
http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
"""

blue = np.uint8([[[255,0,0 ]]])
green = np.uint8([[[0,255,0 ]]])
red = np.uint8([[[0,0,255 ]]])

hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

print("converting from bgr blue :", blue)
print("to")
print("hsv blue :", hsv_blue)
print()
print("converting from bgr green :", green)
print("to")
print("hsv green :", hsv_green)
print()
print("converting from bgr red :", red)
print("to")
print("hsv red :", hsv_red)

