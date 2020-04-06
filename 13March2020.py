import cv2
import numpy as np

img = cv2.imread("flower.jpg",1)
print(img)

shape = img.shape
print("Original img shape--->",img)
print(shape)
print("Resized Iamge---->")
resizedimg = cv2.resize(img,(shape[0]//2, shape[1]//2))
cv2.imshow("resized Flower Img--->\n",resizedimg)
print(resizedimg)
shape2 = resizedimg.shape
print("Resized Flower Img shape--->",img)
print(shape2)
print("Resized Imge---->")


rotatedimg = np.rot90(resizedimg)
print(rotatedimg)

cv2.imshow("rotated img is like-->",rotatedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()