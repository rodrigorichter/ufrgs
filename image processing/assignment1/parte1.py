import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('spacex.jpg',0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.imwrite('spacegrey.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()