import cv2
import time
 
vc = cv2.VideoCapture(0)

if vc.isOpened(): 
    print("test")
    rval, frame = vc.read()
else:
    pass


windowName = "my video cam"


while True:
    cv2.imshow(windowName, frame)
    rval, frame = vc.read();

    # 'ESC' for quit
    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.imshow(windowName, frame)
key = cv2.waitKey(0)

cv2.destroyWindow(windowName)