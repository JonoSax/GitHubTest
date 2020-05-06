#The purpose of this script is to assess the difference in image information between the raw tif file and a compressed jpg file
#What i am looking for here is to assess whether I can use jpg files to process with minimal information loss because the file 
#sizes are at least a tenth the size of the tif files (!) but is there valuable info being lost??

import numpy as np
import cv2
from matplotlib import pyplot as plt

#load in the images
imgJPG = cv2.cvtColor(cv2.imread('testWHOLE.jpg'), cv2.COLOR_BGR2RGB)
imgTIF = cv2.cvtColor(cv2.imread('testWHOLE.tif'), cv2.COLOR_BGR2RGB)

#compute the RGB difference between jpg and tif
diff = imgJPG - imgTIF

#plotting the jpg, tif and difference of the two
plt.subplot(1, 3, 1), plt.imshow(imgJPG)
plt.subplot(1, 3, 2), plt.imshow(imgTIF)
plt.subplot(1, 3, 3), plt.imshow(diff)

plt.show()

#convert the difference into a gray scale intensity
diffINT = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
plt.imshow(diffINT, 'gray')
plt.show()

print("finish")