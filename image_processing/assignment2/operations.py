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
		panelA.grid(row=7,column=0)

		panelB = Label(image=displayedImage2)
		panelB.image = displayedImage2
		panelB.grid(row=7,column=1)

		panelC = Label(image=displayedImage3)
		panelC.image = displayedImage3
		panelC.grid(row=7,column=2)
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
	amount = float(contrastEntry.get())
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

	biggestValue=0

	for i in range(0,256):
		if histogramDict[i] > biggestValue:
			biggestValue = histogramDict[i]
	print(biggestValue)
	for key, value in histogramDict.items():
		histogramDict[key] = (histogramDict[key]/float((img2.shape[0]*img2.shape[1])))*biggestValue

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
	
	for c in range(0,3):
		i = 0
		while i < img2.shape[0]-sX:
			j=0
			while j < img2.shape[1]-sY:
				total = 0
				for x in range(i,i+sX):
					for y in range(j,j+sY):
						total+=img2[x,y,c]
				avg = total/(sX*sY)
				newImg[i/sX,j/sY,c] = avg
				j+=sY
			i+=sX

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

def zoomIn():
	global img2
	global img3
	newImg = np.full((img2.shape[0]*2,img2.shape[1]*2,3), 255, np.uint8)

	i = 0
	while i < newImg.shape[0]:
		j = 0
		while j < newImg.shape[1]:
			newImg[i,j,:] = img2[i/2,j/2,:]
			j+=2
		i+=2

	i = 0
	while i < newImg.shape[0]:
		j = 1
		while j < newImg.shape[1]-1:
			newImg[i,j,0] = (int(newImg[i,j+1,0]) + newImg[i,j-1,0])/2
			newImg[i,j,1] = (int(newImg[i,j+1,1]) + newImg[i,j-1,1])/2
			newImg[i,j,2] = (int(newImg[i,j+1,2]) + newImg[i,j-1,2])/2
			j+=2
		i+=2
	
	i = 1
	while i < newImg.shape[0]-1:
		j = 0
		while j < newImg.shape[1]:
			newImg[i,j,0] = (int(newImg[i+1,j,0]) + newImg[i-1,j,0])/2
			newImg[i,j,1] = (int(newImg[i+1,j,1]) + newImg[i-1,j,1])/2
			newImg[i,j,2] = (int(newImg[i+1,j,2]) + newImg[i-1,j,2])/2
			j+=1
		i+=2

	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

def rotateClockWise():
	global img2
	global img3

	newImg = np.full((img2.shape[1],img2.shape[0],3), 255, np.uint8)

	for i in range(newImg.shape[0]):
		for j in range(newImg.shape[1]):
			newImg[i,j,:] = (img2[j,i,:]+0)

	img2 = copy.deepcopy(newImg)
	flipHorizontal()
	updateImagesInScreen()

def rotateAntiClockWise():
	global img2
	global img3
	flipHorizontal()
	newImg = np.full((img2.shape[1],img2.shape[0],3), 255, np.uint8)

	for i in range(newImg.shape[0]):
		for j in range(newImg.shape[1]):
			newImg[i,j,:] = (img2[j,i,:]+0)

	img2 = copy.deepcopy(newImg)
	
	updateImagesInScreen()

def convolute():
	global img2
	global img3

	newImg = np.full((img2.shape[0],img2.shape[1],3), 255, np.uint8)

	for i in range(1,newImg.shape[0]-1):
		for j in range(1,newImg.shape[1]-1):
			print('before',img2[i,j,:])
			newImg[i,j,:] = img2[i-1,j-1,:]*float(Conv20Entry.get()) + img2[i,j-1,:]*float(Conv21Entry.get()) + img2[i+1,j-1,:]*float(Conv22Entry.get()) + img2[i-1,j,:]*float(Conv10Entry.get()) + img2[i,j,:]*float(Conv11Entry.get()) + img2[i+1,j,:]*float(Conv12Entry.get()) + img2[i-1,j+1,:]*float(Conv00Entry.get()) + img2[i,j+1,:]*float(Conv01Entry.get()) + img2[i+1,j+1,:]*float(Conv02Entry.get())
			print('after',newImg[i,j,:])
	img2 = copy.deepcopy(newImg)
	updateImagesInScreen()

root = Tk()
panelA = None
panelB = None
img = None
img2 = None
img3 = None

ConvolutionLabel = Label(root, text="Convolute").grid(row=0,column=0)
Conv00Entry = Entry(root, bd =5)
Conv01Entry = Entry(root, bd =5)
Conv02Entry = Entry(root, bd =5)
Conv10Entry = Entry(root, bd =5)
Conv11Entry = Entry(root, bd =5)
Conv12Entry = Entry(root, bd =5)
Conv20Entry = Entry(root, bd =5)
Conv21Entry = Entry(root, bd =5)
Conv22Entry = Entry(root, bd =5)
Conv00Entry.grid(row=1,column=0)
Conv01Entry.grid(row=1,column=1)
Conv02Entry.grid(row=1,column=2)
Conv10Entry.grid(row=2,column=0)
Conv11Entry.grid(row=2,column=1)
Conv12Entry.grid(row=2,column=2)
Conv20Entry.grid(row=3,column=0)
Conv21Entry.grid(row=3,column=1)
Conv22Entry.grid(row=3,column=2)

brightnessLabel = Label(root, text="Brightness").grid(row=4,column=0)
brightnessEntry = Entry(root, bd =5)
brightnessEntry.grid(row=4,column=1)
contrastLabel = Label(root, text="Contrast").grid(row=5,column=0)
contrastEntry = Entry(root, bd =5)
contrastEntry.grid(row=5,column=1)

zoomOutLabel = Label(root, text="ZoomOut").grid(row=6,column=0)
zoomOutXEntry = Entry(root, bd =5)
zoomOutXEntry.grid(row=6,column=1)
zoomOutYEntry = Entry(root, bd =5)
zoomOutYEntry.grid(row=6,column=2)

selectImageBtn = Button(root, text="Select an image", command=selectImage).grid(row=0,column=3)
horizontalBtn = Button(root, text ="Flip Horizontally", command = flipHorizontal).grid(row=1,column=3)
grayscaleBtn = Button(root, text ="Grayscale", command = grayscale).grid(row=2,column=3)
histogramBtn = Button(root, text ="Generate Histogram", command = generateHistogram).grid(row=3,column=3)
brightnessBtn = Button(root, text ="Change Brightness", command = changeBrightness).grid(row=4,column=3)
contrastBtn = Button(root, text ="Change Contrast", command = changeContrast).grid(row=5,column=3)
negativeBtn = Button(root, text ="Negative", command = negative).grid(row=6,column=3)
equalizeBtn = Button(root, text ="Equalize", command = equalize).grid(row=7,column=3)
zoomOutBtn = Button(root, text ="ZoomOut", command = zoomOut).grid(row=8,column=3)
zoomInBtn = Button(root, text ="ZoomIn", command = zoomIn).grid(row=9,column=3)
rotateClockWiseBtn = Button(root, text ="rotateClockWise", command = rotateClockWise).grid(row=10,column=3)
rotateAntiClockWiseBtn = Button(root, text ="rotateAntiClockWise", command = rotateAntiClockWise).grid(row=11,column=3)
convoluteBtn = Button(root, text ="Convolute", command = convolute).grid(row=12,column=3)

root.mainloop()