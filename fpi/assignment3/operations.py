import numpy as np
import cv2
import copy

def nothing(x):
	pass

cv2.namedWindow('Original Video', cv2.WINDOW_NORMAL)
cv2.namedWindow('Result Video', cv2.WINDOW_NORMAL)

# Create trackbars
flipGaussianBlurLevel = 'GaussianBlur'
cv2.createTrackbar(flipGaussianBlurLevel, 'Original Video',0,255,nothing)

flipBrightnessLevel = 'Brightness'
cv2.createTrackbar(flipBrightnessLevel, 'Original Video',0,255,nothing)

flipContrastLevel = 'Contrast'
cv2.createTrackbar(flipContrastLevel, 'Original Video',0,255,nothing)

gaussianBlurIsActive = False
cannyIsActive = False
sobelIsActive = False
brightnessIsActive = False
contrastIsActive = False
negativeIsActive = False
grayscaleIsActive = False
resizeIsActive = False
rotateIsActive = False
horizontalFlipIsActive = False
verticalFlipIsActive = False

vc = cv2.VideoCapture(0)


if vc.isOpened():
	rval, frame = vc.read()
	resultFrame = copy.deepcopy(frame)
else:
	rval = False

fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1],frame.shape[0]))

while rval:
	if vc.isOpened():
		rval, frame = vc.read()
	else:
		rval = False

	key = cv2.waitKey(1)
	if key == 27:
		break
	if key == ord('q'):
		if gaussianBlurIsActive == True:
			gaussianBlurIsActive = False
		else:
			gaussianBlurIsActive = True
	if key == ord('w'):
		if cannyIsActive == True:
			cannyIsActive = False
		else:
			cannyIsActive = True
	if key == ord('e'):
		if sobelIsActive == True:
			sobelIsActive = False
		else:
			sobelIsActive = True
	if key == ord('r'):
		if brightnessIsActive == True:
			brightnessIsActive = False
		else:
			brightnessIsActive = True
	if key == ord('t'):
		if contrastIsActive == True:
			contrastIsActive = False
		else:
			contrastIsActive = True
	if key == ord('y'):
		if negativeIsActive == True:
			negativeIsActive = False
		else:
			negativeIsActive = True
	if key == ord('u'):
		if grayscaleIsActive == True:
			grayscaleIsActive = False
		else:
			grayscaleIsActive = True
	if key == ord('i'):
		if resizeIsActive == True:
			resizeIsActive = False
		else:
			resizeIsActive = True
	if key == ord('o'):
		if rotateIsActive == True:
			rotateIsActive = False
		else:
			rotateIsActive = True
	if key == ord('p'):
		if horizontalFlipIsActive == True:
			horizontalFlipIsActive = False
		else:
			horizontalFlipIsActive = True
	if key == ord('a'):
		if verticalFlipIsActive == True:
			verticalFlipIsActive = False
		else:
			verticalFlipIsActive = True

	cv2.imshow('Original Video', frame)

	resultFrame = copy.deepcopy(frame)

	if gaussianBlurIsActive:
		kSize = cv2.getTrackbarPos(flipGaussianBlurLevel,'Original Video')
		if kSize % 2 == 0:
			kSize-=1
		resultFrame = copy.deepcopy(cv2.GaussianBlur(frame,(kSize,kSize),30))
	elif cannyIsActive:
		resultFrame = copy.deepcopy(cv2.Canny(frame,100,100))
		resultFrame = copy.deepcopy(cv2.cvtColor(resultFrame,cv2.COLOR_GRAY2RGB))
	elif sobelIsActive:
		resultFrame = copy.deepcopy(cv2.Sobel(frame,cv2.CV_8U,1,1,ksize=7))
	elif brightnessIsActive:
		amount = cv2.getTrackbarPos(flipBrightnessLevel,'Original Video')
		resultFrame = cv2.add(frame, np.full((frame.shape[0],frame.shape[1],3), amount, np.uint8))
	elif contrastIsActive:
		amount = cv2.getTrackbarPos(flipContrastLevel,'Original Video')
		resultFrame = cv2.multiply(frame, np.full((frame.shape[0],frame.shape[1],3), amount, np.uint8))
	elif negativeIsActive:
		resultFrame = 255-frame
	elif grayscaleIsActive:
		resultFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		resultFrame = copy.deepcopy(cv2.cvtColor(resultFrame,cv2.COLOR_GRAY2RGB))
	elif resizeIsActive:
		resultFrame = cv2.resize(frame,((frame.shape[0])/2,(frame.shape[1])/2))
	elif rotateIsActive:
		rows=frame.shape[0]
		cols=frame.shape[1]
		resultFrame = cv2.warpAffine(frame, cv2.getRotationMatrix2D((cols/2,rows/2),90,1),(cols,rows))
	elif horizontalFlipIsActive:
		resultFrame = cv2.flip(frame,1)
	elif verticalFlipIsActive:
		resultFrame = cv2.flip(frame,0)

	frame = copy.deepcopy(resultFrame)

	cv2.imshow('Result Video',frame)
	out.write(frame)	

vc.release()
out.release()
cv2.destroyWindow('Original Video')
cv2.destroyWindow('Result Video')


#cd dev/u*/i*/a*3