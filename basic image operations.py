import cv2


img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)  # return a tuple of numer of row, colums, and channels
print(img.size)  # returns Total number of pixels is accessed
print(img.dtype)  # returns image datatype is obtained

ball = img[280:340, 330:390]  # copying ball coordinates
img[273:333, 100:160] = ball  # assign ball to copy to new coordinates
cv2.imshow('image', img)

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
cv2.imshow('image Resize', img)

#dst = cv2.add(img, img2)  # add to images together
dst = cv2.addWeighted(img, .1, img2, .9, 0)  # src1: first array, alpha: weight of first array, src2: second array, beta:weight of
# second array, gamma: scalar added to each sum

cv2.imshow('combine', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
