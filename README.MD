This project is experiments on opencv3.X


## Preparing virtual environment
```
brew instll openv
pip install virtualenv virtualenvwrapper
mkvirtualenv cv -p python3
cd ~/.virtualenvs/cv
echo /usr/local/opt/opencv3/lib/python3.6/site-packages >> ~/.virtualenvs/cv/lib/python3.6/site-packages/opencv3.pth
```

## How to execute : python

```
workon cv
python -m opencvutil.01_opencv_basic.01_opencv_mac -i images/mac/mac-01.jpg
```


## Table of Contents

- [01_opencv_basic](#Trying-out-core-functionality-of-opencv)
- [02_image_preprocessing](#Image-Preprocessing)

## Trying out core functionality of opencv

- [x] **opencvutil.01_opencv_basic.01_opencv_mac** : display an image
- [x] **pencvutil.01_opencv_basic.02_opencv_image** : display image by mpl(e.g. matplotlib)
- [x] **opencvutil.01_opencv_basic.03_opencv_basicops.py** : handling the image and access pixels
- [x] **opencvutil.01_opencv_basic.04_opencv_image_arithmetics**
- [x] opencvutil.01_opencv_basic.05_opencv_open_cv.py** : open camera and see yourself
- [x] **opencvutil.01_opencv_basic.06_opencv_bgr_to_hsv.py** : convert color space

## Image Preprocessing 
- [x] **opencvutil.02_image_preprocessing.01_image_pyramids** : image pyramids
- [x] **opencvutil.02_image_preprocessing.02_sliding_window** : sliding windows of a image
- [x] **opencvutil.02_image_preprocessing.03_sliding_window_batch** : batching processing sliding windows of images 

## References

* [opencv-python-tutorial](http://docs.opencv.org/master/)).
* [Image Pyramids with Python and OpenCV](http://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/)