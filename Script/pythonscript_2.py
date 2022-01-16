# Resize an Image by scale
import sys
import cv2

path = sys.argv[1]
scale = int(sys.argv[2])

oldImage = cv2.imread(path)
newSize = (oldImage.shape[1] // scale, oldImage.shape[0] // scale)
print(newSize)
print(oldImage.shape)
newImage = cv2.resize(oldImage, newSize, interpolation=cv2.INTER_AREA)

cv2.imwrite("new.jpg", newImage)