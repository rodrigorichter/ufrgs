import numpy as np
import copy

amountOfNodes = 0

class Node:
	def __init__(self):
		self.children = []
		global amountOfNodes
		self.id = amountOfNodes-1
		amountOfNodes += 1
		self.distanceFromParent = 0



# Initiate distance Mat
def initDistMat():
	distMat = np.zeros((5,5))

	distMat[0][1] = 0.189
	distMat[0][2] = 0.11
	distMat[0][3] = 0.113
	distMat[0][4] = 0.215

	distMat[1][0] = 0.189
	distMat[1][2] = 0.179
	distMat[1][3] = 0.192
	distMat[1][4] = 0.211

	distMat[2][0] = 0.11
	distMat[2][1] = 0.179
	distMat[2][3] = 0.09405
	distMat[2][4] = 0.205

	distMat[3][0] = 0.113
	distMat[3][1] = 0.192
	distMat[3][2] = 0.0940
	distMat[3][4] = 0.2140

	distMat[4][0] = 0.215
	distMat[4][1] = 0.211
	distMat[4][2] = 0.205
	distMat[4][3] = 0.214

	return distMat

# start nodes
def startNodes():
	root = Node()
	root.children = [Node(),Node(),Node(),Node(),Node()]
	return root

# calculate new distMat
def updateDistMat(distMat, pair):
	matSize = distMat.shape[0]

	distMat = np.insert(copy.deepcopy(distMat),matSize,0,axis=1)
	distMat = np.insert(copy.deepcopy(distMat),matSize,0,axis=0)

	# find distance from the rest of taxa to the new node
	matSize = distMat.shape[0]

	for i in range(matSize):
		distMat[matSize-1][i] = (1/2.0)*(distMat[pair[0]][i] + distMat[pair[1]][i] - distMat[pair[0]][pair[1]])
		distMat[i][matSize-1] = copy.deepcopy(distMat[matSize-1][i])
		print(distMat[i][matSize-1])
	print(distMat)

	distMat = np.delete(distMat,(pair[1]),axis=0)
	distMat = np.delete(distMat,(pair[1]),axis=1)
	distMat = np.delete(distMat,(pair[0]),axis=0)
	distMat = np.delete(distMat,(pair[0]),axis=1)

	return distMat
	
# find q Mat from distMat
def findQMat(distMat):
	matSize = distMat.shape[0]
	qMat = np.zeros((matSize,matSize))

	for i in range(matSize):
		for j in range(matSize):
			s1 = 0
			for k in range(matSize):
				s1+=distMat[i][k]
			s2 = 0
			for k in range(matSize):
				s2+=distMat[j][k]

			qMat[i][j] = (5-2)*distMat[i][j] - s1 - s2
	return qMat

# find pair of distinct taxa with lowest value in q Mat
def findSmallestPair(qMat):
	smallest = 999999
	smallestIJ = []
	for i in range(0,qMat.shape[0]):
		for j in range(0,qMat.shape[0]):
			if i != j and qMat[i][j] < smallest:
				smallest = qMat[i][j]
				smallestIJ = [i,j]
	
	return smallestIJ

# generate new node from pair and add to the tree
def updateTree(distMat, smallestPair, root):
	newNode = Node()
	newNode.id = distMat.shape[0]-2

	i = 0
	while i < len(root.children):
		if root.children[i].id == smallestPair[0] or root.children[i].id == smallestPair[1]:
			newNode.children.append(copy.deepcopy(root.children[i]))
			print('achou')
			root.children.pop(i)
			i-=1
		i+=1

	matSize = distMat.shape[0]

	# find distance from pair to the newly created node
	s1 = 0
	for k in range(0,matSize):
		s1+=distMat[smallestPair[0]][k]
	s2 = 0
	for k in range(0,matSize):
		s2+=distMat[smallestPair[1]][k]

	newNode.children[0].distanceFromParent = (1/2.0)*(distMat[smallestPair[0],smallestPair[1]])+(1/6.0)*(s1-s2)
	newNode.children[1].distanceFromParent = distMat[smallestPair[0]][smallestPair[1]] - distMat[matSize-1][smallestPair[0]]

	root.children.append(newNode)

# main
distMat = initDistMat()
distMatIdxs = {}
root = startNodes()

for i in range(len(root.children)):
	qMat = findQMat(distMat)
	smallestPair = findSmallestPair(qMat)
	updateTree(distMat,smallestPair,root)
	distMat = updateDistMat(distMat,smallestPair)


	#print(distMat)
