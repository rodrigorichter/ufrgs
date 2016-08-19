import numpy as np
import cv2

def nothing(x):
	pass

# Load images
img = cv2.imread('test_images/Space_187k.jpg',1)
img2 = cv2.imread('test_images/Space_187k.jpg',1)

# Open windows
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Result Image', cv2.WINDOW_NORMAL)

# Create trackbars
flipHorizontalSwitch = 'Horizontal'
cv2.createTrackbar(flipHorizontalSwitch, 'Original Image',0,1,nothing)

flipVerticalSwitch = 'Vertical'
cv2.createTrackbar(flipVerticalSwitch, 'Original Image',0,1,nothing)

flipGreyscaleSwitch = 'Greyscale'
cv2.createTrackbar(flipGreyscaleSwitch, 'Original Image',0,1,nothing)

flipTrackbarQuantizeTrigger = 'QTrigger'
cv2.createTrackbar(flipTrackbarQuantizeTrigger,'Original Image',0,1,nothing)

flipTrackbarQuantizeLevel = 'QLevel'
cv2.createTrackbar(flipTrackbarQuantizeLevel,'Original Image',0,255,nothing)

flipResetSwitch = 'Reset'
cv2.createTrackbar(flipResetSwitch, 'Original Image',0,1,nothing)

flipSaveSwitch = 'Save'
cv2.createTrackbar(flipSaveSwitch, 'Result Image',0,1,nothing)

horizontalSwitchCurrent = 0
verticalSwitchCurrent = 0
greyscaleSwitchCurrent = 0
trackbarQuantizeTriggerCurrent = 0
trackbarQuantizeLevelCurrent = 0
resetSwitchCurrent = 0
saveSwitchCurrent = 0

while(1):
	cv2.imshow('Original Image',img)
	cv2.imshow('Result Image',img2)

	horizontalSwitchNew = cv2.getTrackbarPos(flipHorizontalSwitch,'Original Image')
	verticalSwitchNew = cv2.getTrackbarPos(flipVerticalSwitch,'Original Image')
	greyscaleSwitchNew = cv2.getTrackbarPos(flipGreyscaleSwitch,'Original Image')
	trackbarQuantizeTriggerNew = cv2.getTrackbarPos(flipTrackbarQuantizeTrigger,'Original Image')
	trackbarQuantizeLevelNew = cv2.getTrackbarPos(flipTrackbarQuantizeLevel,'Original Image')
	resetSwitchNew = cv2.getTrackbarPos(flipResetSwitch,'Original Image')
	saveSwitchNew = cv2.getTrackbarPos(flipSaveSwitch,'Result Image')

	if horizontalSwitchNew != horizontalSwitchCurrent:
		img2 = img2[:,::-1]
		horizontalSwitchCurrent = horizontalSwitchNew

	if verticalSwitchNew != verticalSwitchCurrent:
		img2 = img2[::-1,:]
		verticalSwitchCurrent = verticalSwitchNew

	if greyscaleSwitchNew != greyscaleSwitchCurrent:
		if greyscaleSwitchNew == 1:
			for i in range (0, img2.shape[0]):
				for j in range (0, img2.shape[1]):
					pixel = img2[i][j]
					l = pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114
					img2[i][j].fill(l)
		greyscaleSwitchCurrent = greyscaleSwitchNew

	if trackbarQuantizeTriggerNew != trackbarQuantizeTriggerCurrent:
		amountOfShades = trackbarQuantizeLevelNew
		qLevel = int(255/amountOfShades)

		for i in range (0, img2.shape[0]):
			for j in range (0, img2.shape[1]):
				pixel = img2[i][j]
				roundError = pixel[0] % qLevel
				if roundError != 0:
					if roundError < qLevel:
						img2[i][j].fill(pixel[0]-roundError)
					elif roundError == qLevel:
						img2[i][j].fill(0)

		trackbarQuantizeTriggerCurrent = trackbarQuantizeTriggerNew

	if resetSwitchNew != resetSwitchCurrent:
		if resetSwitchNew == 1:
			img2 = np.copy(img)
		resetSwitchCurrent = resetSwitchNew

	if saveSwitchNew != saveSwitchCurrent:
		cv2.imwrite('test_images/Space_187k_new.jpg',img2)
		verticalSwitchCurrent = verticalSwitchNew

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break









cv2.destroyAllWindows()