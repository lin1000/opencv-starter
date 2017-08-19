import numpy as np
import cv2
from matplotlib import pyplot as plt

#http://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html

# Load an color image in grayscale
img = cv2.imread('../images/mac/mac-01.jpg')

#Using matplotlib to show image
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


#using open cv to show image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('copyOfImage.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


