import cv2
#import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('t1.png')
grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)

print(ret,thresh1)

plt.imshow(thresh1)
plt.show()