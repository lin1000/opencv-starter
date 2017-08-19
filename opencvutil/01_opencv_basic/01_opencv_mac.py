# USAGE
# python 01_opencv_mac.py -i ../images/mac/mac_01.jpg

# import the necessary packages
import argparse
import cv2
import matplotlib.pyplot as plt
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])

print(type(image))

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
          

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
## load the cat detector Haar cascade, then detect cat faces
## in the input image
#detector = cv2.CascadeClassifier(args["cascade"])
#rects = detector.detectMultiScale(gray, scaleFactor=1.3,
#	minNeighbors=10, minSize=( 75, 75))
#
## loop over the cat faces and draw a rectangle surrounding each
#for (i, (x, y, w, h)) in enumerate(rects):
#	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#	cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
#		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
#
## show the detected cat faces
#cv2.imshow("Cat Faces", image)
#cv2.waitKey(0)
