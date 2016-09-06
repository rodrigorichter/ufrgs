import numpy as np
import cv2
import copy

def nothing(x):
	pass

def loadImage(address):
	return cv2.imread(address,1)

def newWindow(name):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)

def flipHorizontal(img):
	return img[:,::-1]

def changeBrightness(img, amount, channel):
	newImg = copy.deepcopy(img)

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if img[i][j][channel] + amount > 255:
				newImg[i][j][channel] = 255
			elif img[i][j][channel] + amount < 0:
				newImg[i][j][channel] = 0
			else:
				newImg[i][j][channel]+=amount

	return newImg

def changeContrast(img, amount, channel):
	newImg = copy.deepcopy(img)

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if img[i][j][channel] * amount > 255:
				newImg[i][j][channel] = 255
			elif img[i][j][channel] * amount < 0:
				newImg[i][j][channel] = 0
			else:
				newImg[i][j][channel]*=amount

	return newImg

def negative(img, channel):
	newImg = copy.deepcopy(img)

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
				newImg[i][j][channel] = 255 - newImg[i][j][channel]

	return newImg

def grayscale(img):
		for i in range (img.shape[0]):
			for j in range (img.shape[1]):
				pixel = img[i][j]
				l = pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114
				img[i][j].fill(l)

def generateHistogram(img):
	#if image is colored
	if (img[0][0][0] != img[0][0][1]):
		grayscale(img)

	histogramDict = {}

	for i in range (img.shape[0]):
			for j in range (img.shape[1]):
				pixel = img[i][j]
				if pixel[0] in histogramDict:
					histogramDict[pixel[0]]+=1
				else:
					histogramDict[pixel[0]] = 1

	for key, value in histogramDict.items():
		print(histogramDict[key])
		histogramDict[key] = (histogramDict[key]/float((img.shape[0]*img.shape[1])))*255
		print(histogramDict[key])

	amountOfPixels = img2.shape[0]*img2.shape[1]
	imgHistogram = np.full((256,256,3), 255, np.uint8)

	for i in range(imgHistogram.shape[0]):
		imgHistogram[255-histogramDict[i]:255,i] = (0,0,0)

	return imgHistogram

def generateCumulativeHistogram(imgHistogram):
	alpha = 255.0/imgHistogram.shape[0]*imgHistogram.shape[1]
	imgCumulativeHistogram = np.full((256,256,3), 255, np.uint8)

	imgCumulativeHistogram[:,0] = alpha*imgHistogram[:,0]
	for i in range(1,256):
		imgCumulativeHistogram[:,i] = imgCumulativeHistogram[:,i-1] + alpha*imgHistogram[:,i]

	return imgCumulativeHistogram

class Trackbar:
	def __init__(self, name, windowName, start, end):
		self.name = name
		self.windowName = windowName
		self.start = start
		self.end = end
		self.switch = 0
		cv2.createTrackbar(name,windowName,start,end,nothing)

	def getSwitch(self):
		return self.switch

	def hasBeenTriggered(self):
		GUISwitch = cv2.getTrackbarPos(self.name,self.windowName)
		if GUISwitch != self.switch:
			self.switch = GUISwitch
			return 1
		else:
			return 0

	def getCurrentValue(self):
		return cv2.getTrackbarPos(self.name,self.windowName)

# Load images
img = loadImage('test_images/Space_187k.jpg')
img2 = loadImage('test_images/Space_187k.jpg')

# Open windows
newWindow('Original Image')
newWindow('Result Image')

# Create trackbars
horizontalTrackbar = Trackbar('Horizontal', 'Original Image',0,1)
grayscaleTrackbar = Trackbar('Grayscale', 'Original Image',0,1)
histogramTrackbar = Trackbar('Histogram', 'Result Image',0,1)
addBrightnessTrackbar = Trackbar('AddBrightness', 'Original Image',0,255)
subBrightnessTrackbar = Trackbar('SubBrightness', 'Original Image',0,255)
triggerBrightnessTrackbar = Trackbar('TrigBrightness', 'Original Image',0,1)
contrastTrackbar = Trackbar('Contrast', 'Original Image',0,255)
triggerContrastTrackbar = Trackbar('TrigContrast', 'Original Image',0,1)
negativeTrackbar = Trackbar('Negative', 'Original Image',0,1)
equalizeTrackbar = Trackbar('Equalize', 'Original Image',0,1)

while(1):
	cv2.imshow('Original Image',img)
	cv2.imshow('Result Image',img2)

	if horizontalTrackbar.hasBeenTriggered():
		img2 = flipHorizontal(img2)

	if grayscaleTrackbar.hasBeenTriggered():
		grayscale(img2)

	if histogramTrackbar.hasBeenTriggered():
		imgHistogram = generateHistogram(img2)
		
		newWindow('Histogram')
		cv2.imshow('Histogram',imgHistogram)

	if triggerBrightnessTrackbar.hasBeenTriggered():
		brightness = addBrightnessTrackbar.getCurrentValue()
		brightness-= subBrightnessTrackbar.getCurrentValue()
		img2 = changeBrightness(img2, brightness, 0)
		img2 = changeBrightness(img2, brightness, 1)
		img2 = changeBrightness(img2, brightness, 2)

	if triggerContrastTrackbar.hasBeenTriggered():
		contrast = contrastTrackbar.getCurrentValue()
		img2 = changeContrast(img2, contrast, 0)
		img2 = changeContrast(img2, contrast, 1)
		img2 = changeContrast(img2, contrast, 2)

	if negativeTrackbar.hasBeenTriggered():
		img2 = negative(img2, 0)
		img2 = negative(img2, 1)
		img2 = negative(img2, 2)

	if equalizeTrackbar.hasBeenTriggered():
		imgHistogram = generateHistogram(img2)
		imgCumulativeHistogram = generateCumulativeHistogram(imgHistogram)
		
		for i in range (img2.shape[0]):
			for j in range (img2.shape[1]):
				img2[i][j] = imgCumulativeHistogram[img2[i][j][0]][255]

		newWindow('CHistogram')
		cv2.imshow('CHistogram',img2)

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break


cv2.destroyAllWindows()