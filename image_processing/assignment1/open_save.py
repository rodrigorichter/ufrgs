import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('test_images/Gramado_22k.jpg',1)
img2 = cv2.imread('test_images/Gramado_72k.jpg',1)
img3 = cv2.imread('test_images/Space_46k.jpg',1)
img4 = cv2.imread('test_images/Space_187k.jpg',1)
img5 = cv2.imread('test_images/Underwater_53k.jpg',1)

cv2.imwrite('test_images/Gramado_22k_new.jpg',img)
cv2.imwrite('test_images/Gramado_72k_new.jpg',img2)
cv2.imwrite('test_images/Space_46k_new.jpg',img3)
cv2.imwrite('test_images/Space_187k_new.jpg',img4)
cv2.imwrite('test_images/Underwater_53k_new.jpg',img5)