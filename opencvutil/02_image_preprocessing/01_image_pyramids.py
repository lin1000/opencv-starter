#http://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/
from skimage.transform import pyramid_gaussian
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Path to the image(no default)")
parser.add_argument("-s", "--scale", type=float, default=1.5, help="scale factor size (default:%(default).1f)")
args = vars(parser.parse_args())

if( len( args ) == 0):
    parser.print_help()
    sys.exit(1)

# load the image
image = cv2.imread(args["image"])


# METHOD #2: Resizing + Gaussian smoothing.
for (i, resized) in enumerate(pyramid_gaussian(image, downscale=args["scale"])):
# if the image is too small, break from the loop
    if resized.shape[0] < 30 or resized.shape[1] < 30:
        break
    # show the resized image
    cv2.imshow("Layer {}".format(i + 1), resized)
    cv2.waitKey(0)

