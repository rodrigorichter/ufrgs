import numpy as np
import cv2

def nothing(x):
	pass

# Load images
img = cv2.imread('spacex.jpg',1)
img2 = cv2.imread('spacex.jpg',1)

# Open windows
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)

# Create trackbars
flipHorizontalSwitch = 'Horizontal'
cv2.createTrackbar(flipHorizontalSwitch, 'image',0,1,nothing)
flipVerticalSwitch = 'Vertical'
cv2.createTrackbar(flipVerticalSwitch, 'image',0,1,nothing)
flipGreyscaleSwitch = 'Greyscale'
cv2.createTrackbar(flipGreyscaleSwitch, 'image',0,1,nothing)
cv2.createTrackbar(flipTrackbarQuantizate,'image',0,255,nothing)
flipResetSwitch = 'Reset'
cv2.createTrackbar(flipResetSwitch, 'image',0,1,nothing)

horizontalSwitchCurrent = 0
verticalSwitchCurrent = 0
greyscaleSwitchCurrent = 0
trackbarQuantizateCurrent = 0
resetSwitchCurrent = 0

while(1):
	cv2.imshow('image',img)
	cv2.imshow('image2',img2)

	horizontalSwitchNew = cv2.getTrackbarPos(flipHorizontalSwitch,'image')
	verticalSwitchNew = cv2.getTrackbarPos(flipVerticalSwitch,'image')
	greyscaleSwitchNew = cv2.getTrackbarPos(flipGreyscaleSwitch,'image')
	trackbarQuantizateNew = cv2.getTrackbarPos(flipTrackbarQuantizate,'image')
	resetSwitchNew = cv2.getTrackbarPos(flipResetSwitch,'image')

	if horizontalSwitchNew != horizontalSwitchCurrent:
		img2 = img2[:,::-1]
		horizontalSwitchCurrent = horizontalSwitchNew

	if verticalSwitchNew != verticalSwitchCurrent:
		img2 = img2[::-1,:]
		verticalSwitchCurrent = verticalSwitchNew

	if greyscaleSwitchNew != greyscaleSwitchCurrent:
		if greyscaleSwitchNew == 1:
			for i in range (0, img.shape[0]):
				for j in range (0, img.shape[1]):
					pixel = img2[i][j]
					l = pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114
					img2[i][j].fill(l)
		greyscaleSwitchCurrent = greyscaleSwitchNew

	if trackbarQuantizateNew != trackbarQuantizateCurrent:
		print('not done')

	if resetSwitchNew != resetSwitchCurrent:
		if resetSwitchNew == 1:
			img2 = img
		resetSwitchCurrent = resetSwitchNew


	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break









cv2.destroyAllWindows()