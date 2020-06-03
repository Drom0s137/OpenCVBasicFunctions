from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts BGR to RGB

plt.imshow(img)
plt.xticks([], plt.yticks([])) # delete x, y coordinates on plt img
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
