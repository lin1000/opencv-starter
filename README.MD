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
cd 01_opencv_basic
python <01_opencv_mac.py>
```


## Table of Contents

- [01_opencv_basic](#updating-to-new-releases)


## Trying out core functionality of opencv

- [x] 01_opencv_mac.py : display an image
- [x] 02_opencv_image.py : display image by mpl(e.g. matplotlib)
- [x] 03_opencv_basicops.py : handling the image and access pixels
- [x] 04_opencv_image_arithmetics.py
- [x] 05_opencv_open_cv.py : open camera and see yourself

## References

* [opencv-python-tutorial](http://docs.opencv.org/master/)).