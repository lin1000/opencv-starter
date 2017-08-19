#http://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../images/mac/mac-01.jpg')


#ndim : number of dimentsion 
print("img.ndim=" + str(img.ndim))

#shape : the "shape" of this image 
print("img.shape(y,x,channels)=" + str(img.shape))

#dtype : in this case unsigned integer of 8 bit
print("img.dtype=" + str(img.dtype))

#pickup a point in array operator : in this case [102 101 111]
print("img[1, 2]=" + str(img[1,2]))
print("type(img[1, 2])=" + str(type(img[1,2])))
print("img[1, 2].shape=" + str(img[1,2].shape))

#access first column of every row 
firstColumOfEveryRow = img[:,1]
print("img height="+str(len(firstColumOfEveryRow)))
print(firstColumOfEveryRow)

#access first row of every column
firstRowOfEveryColumn = img[1:]
print(firstRowOfEveryColumn)
print("img width="+str(len(firstRowOfEveryColumn)))

#itemsize : number of bytes of single pixel
print("itemsize=" + str(img.itemsize))

#size : number of pixel points in the image
print("size="+ str(img.size))

##access RED value of a pixel
print(img.item(10,10,2))


for i in range(1,1000):
    for j in range(1,1000):
        img.itemset((i,j,2),100)


##access RED value of a pixel
print(img.item(10,10,2))

## Copy a ROI into another place
keystroke = img[1000:1300, 1000:1300]
img[3000:3300,2000:2300] = keystroke

#using open cv to show image
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

constant= cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT,value=[0,0,255])
reflect= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT,value=[0,0,255])

plt.subplot(221),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.subplot(224),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.show()  