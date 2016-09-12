import numpy as np
import cv2
import copy
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog


def selectImage():
	global panelA, panelB, panelC
	global img, img2

	path = tkFileDialog.askopenfilename()

	if len(path) > 0:
		#img = loadImage('test_images/Space_187k.jpg')
		#img2 = loadImage('test_images/Space_187k.jpg')
		
		img = loadImage(path)
		img2 = loadImage(path)
		img3 = loadImage(path)

		displayedImage = imgCvToTk(img)
		displayedImage2 = imgCvToTk(img2)
		displayedImage3 = imgCvToTk(img3)

	if panelA is None or panelB is None or panelC is None:
		panelA = Label(image=displayedImage)
		panelA.image = displayedImage
		panelA.pack(side="left", padx=10, pady=10)

		panelB = Label(image=displayedImage2)
		panelB.image = displayedImage2
		panelB.pack(side="bottom", padx=10, pady=10)

		panelC = Label(image=displayedImage3)
		panelC.image = displayedImage3
		panelC.pack(side="right", padx=10, pady=10)
	else:
		# update the pannels
		panelA.configure(image=displayedImage)
		panelB.configure(image=displayedImage2)
		panelC.configure(image=displayedImage3)
		panelA.image = displayedImage
		panelB.image = displayedImage2
		panelC.image = displayedImage3

def nothing(x):
	pass

def loadImage(address):
	return cv2.imread(address,1)

def updateImagesInScreen():
	global img2, img3
	displayImage2 = imgCvToTk(img2)
	displayImage3 = imgCvToTk(img3)
	panelB.configure(image=displayImage2)
	panelB.image = displayImage2
	panelC.configure(image=displayImage3)
	panelC.image = displayImage3

def imgCvToTk(image):
	convertedImg = copy.deepcopy(image)
	convertedImg = cv2.cvtColor(convertedImg, cv2.COLOR_BGR2RGB)
	convertedImg = Image.fromarray(convertedImg)
	convertedImg = ImageTk.PhotoImage(convertedImg)
	return convertedImg

def newWindow(name):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)

def flipHorizontal():
	global img2
	global img3
	img2 = img2[:,::-1]
	updateImagesInScreen()

def changeBrightness():
	global img2
	global img3
	amount = int(brightnessEntry.get())
	newImg = copy.deepcopy(img2)

	for c in range(0, 3):
		for i in range(img2.shape[0]):
			for j in range(img2.shape[1]):
				if img2[i][j][c] + amount > 255:
					newImg[i][j][c] = 255
				elif img2[i][j][c] + amount < 0:
					newImg[i][j][c] = 0
				else:
					newImg[i][j][c]+=amount

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

def changeContrast():
	global img2
	global img3
	amount = int(contrastEntry.get())
	newImg = copy.deepcopy(img2)

	for c in range(0, 3):
		for i in range(img2.shape[0]):
			for j in range(img2.shape[1]):
				if img2[i][j][c] * amount > 255:
					newImg[i][j][c] = 255
				elif img2[i][j][c] * amount < 0:
					newImg[i][j][c] = 0
				else:
					newImg[i][j][c]*=amount

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

def negative():
	global img2
	global img3
	newImg = copy.deepcopy(img2)

	for c in range(0, 3):
		for i in range(img2.shape[0]):
			for j in range(img2.shape[1]):
					newImg[i][j][c] = 255 - newImg[i][j][c]

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

def grayscale():
	global img2
	global img3
	for i in range (img2.shape[0]):
		for j in range (img2.shape[1]):
			pixel = img2[i][j]
			l = pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114
			img2[i][j].fill(l)
	updateImagesInScreen()

def generateHistogram():
	global img2
	global img3
	#if image is colored
	if (img2[0][0][0] != img2[0][0][1]):
		grayscale()

	histogramDict = {}
	for i in range (img2.shape[0]):
			for j in range (img2.shape[1]):
				pixel = img2[i][j]
				if pixel[0] in histogramDict:
					histogramDict[pixel[0]]+=1
				else:
					histogramDict[pixel[0]] = 1

	for i in range(0,256):
		if i not in histogramDict:
			histogramDict[i] = 0

	for key, value in histogramDict.items():
		histogramDict[key] = (histogramDict[key]/float((img2.shape[0]*img2.shape[1])))*255

	imgHistogram = np.full((256,256,3), 255, np.uint8)

	for i in range(imgHistogram.shape[0]):
		imgHistogram[255-histogramDict[i]:255,i] = (0,0,0)

	img3 = copy.deepcopy(imgHistogram)
	updateImagesInScreen()

def generateCumulativeHistogram(img):
	alpha = 255.0/(img.shape[0]*img.shape[1])
	histogramDict = {}
	cumHistogramDict = {}

	for i in range(0,256):
		if i not in histogramDict:
			histogramDict[i] = 0

	for i in range (img.shape[0]):
			for j in range (img.shape[1]):
				pixel = img[i][j]
				if pixel[0] in histogramDict:
					histogramDict[pixel[0]]+=1
				else:
					histogramDict[pixel[0]] = 1

	cumHistogramDict[0] = alpha*histogramDict[0]
	for i in range(1,256):
		cumHistogramDict[i] = cumHistogramDict[i-1] + alpha*histogramDict[i]
		print('oi:',)

	return cumHistogramDict

def equalize():
	global img2
	global img3
	generateHistogram()
	imgHistogram = copy.deepcopy(img3)
	cumulativeHistogram = generateCumulativeHistogram(img2)
	
	for i in range (img2.shape[0]):
		for j in range (img2.shape[1]):
			img2[i][j] = cumulativeHistogram[img2[i][j][0]]

	updateImagesInScreen()

def zoomOut():
	global img2
	global img3
	sX = int(zoomOutXEntry.get())
	sY = int(zoomOutYEntry.get())
	newImg = np.full((img2.shape[0]/sX,img2.shape[1]/sY,3), 255, np.uint8)
	i = 0
	#for c in range(0,3):
	while i < img2.shape[0]-sX:
		j=0
		while j < img2.shape[1]-sY:
			total = 0
			for x in range(i,i+sX):
				for y in range(j,j+sY):
					total+=img2[x,y,0]
			avg = total/(sX*sY)
			newImg[i/sX,j/sY,:] = avg
			j+=sY
		i+=sX

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()


root = Tk()
panelA = None
panelB = None
img = None
img2 = None
img3 = None




brightnessLabel = Label(root, text="Brightness")
contrastLabel = Label(root, text="Contrast")
zoomOutLabel = Label(root, text="ZoomOut")

brightnessEntry = Entry(root, bd =5)
contrastEntry = Entry(root, bd =5)
zoomOutXEntry = Entry(root, bd =5)
zoomOutYEntry = Entry(root, bd =5)

selectImageBtn = Button(root, text="Select an image", command=selectImage)
horizontalBtn = Button(root, text ="Flip Horizontally", command = flipHorizontal)
grayscaleBtn = Button(root, text ="Grayscale", command = grayscale)
histogramBtn = Button(root, text ="Generate Histogram", command = generateHistogram)
brightnessBtn = Button(root, text ="Change Brightness", command = changeBrightness)
contrastBtn = Button(root, text ="Change Contrast", command = changeContrast)
negativeBtn = Button(root, text ="Negative", command = negative)
equalizeBtn = Button(root, text ="Equalize", command = equalize)
zoomOutBtn = Button(root, text ="ZoomOut", command = zoomOut)

brightnessLabel.pack()
contrastLabel.pack()
zoomOutLabel.pack()

brightnessEntry.pack()
contrastEntry.pack()
zoomOutXEntry.pack()
zoomOutYEntry.pack()

selectImageBtn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
horizontalBtn.pack(side =BOTTOM) 
grayscaleBtn.pack(side =BOTTOM) 
histogramBtn.pack(side =BOTTOM) 
brightnessBtn.pack(side =BOTTOM) 
contrastBtn.pack(side =BOTTOM) 
negativeBtn.pack(side =BOTTOM) 
equalizeBtn.pack(side =BOTTOM) 
zoomOutBtn.pack(side =BOTTOM) 

root.mainloop()
# Load images


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
