import numpy as np
import cv2

def nothing(x):
	pass

def loadImage(address):
	return cv2.imread(address,1)

def newWindow(name):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)

def flipHorizontal(img):
	return img[:,::-1]

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
	return histogramDict

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

while(1):
	cv2.imshow('Original Image',img)
	cv2.imshow('Result Image',img2)

	if horizontalTrackbar.hasBeenTriggered():
		img2 = flipHorizontal(img2)

	if grayscaleTrackbar.hasBeenTriggered():
		grayscale(img2)

	if histogramTrackbar.hasBeenTriggered():
		histogram = generateHistogram(img2)
		amountOfPixels = img2.shape[0]*img2.shape[1]
		imgHistogram = np.zeros((256,256,3), np.uint8)

		for i in range(imgHistogram.shape[0]):
			imgHistogram[i,0:histogram[i]] = (255,255,255)

		newWindow('Histogram')
		cv2.imshow('Histogram',imgHistogram)

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break


cv2.destroyAllWindows()