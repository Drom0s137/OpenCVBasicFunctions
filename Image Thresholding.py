import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # if value less than 127, assign 0, else, assign 1
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # if value less than 127, assign 1, else, assign 0
_, th3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC) # if value more than 200, remain same color
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # if value more than 127, image remain the same

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#cv.waitKey(0)
#cv.destroyAllWindows()