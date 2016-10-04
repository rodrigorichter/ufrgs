
# Read a DNA Sequence
def readSequence():
	sequence = open(raw_input('Enter sequence filename: '),'r')
	sequence.readline()
	sequence = sequence.read().replace('\n', '')
	return sequence

s1 = readSequence()
s2 = readSequence()

L = 10

amountOfSequences = 2

s1list = []
s2list = []

s1mat = []
s2mat = []

nextMat = []

i=0
while i+L < len(s1):
	s1list.append(s1[i:L+i])
	i+=1

i=0
while i+L < len(s2):
	s2list.append(s2[i:L+i])
	i+=1

for i in range(len(s1list)):
	s1mat.append([s1list[i],0,0,0,0])

for i in range(len(s2list)):
	s2mat.append([s2list[i],0,0,0,0])

for i in range(len(s1list)):
	for j in range(L):
		if s1list[i][j] == 'A':
			s1mat[i][1]+=1
		if s1list[i][j] == 'T':
			s1mat[i][2]+=1
		if s1list[i][j] == 'C':
			s1mat[i][3]+=1
		if s1list[i][j] == 'G':
			s1mat[i][4]+=1

for i in range(len(s2list)):
	for j in range(L):
		if s2list[i][j] == 'A':
			s2mat[i][1]+=1
		if s2list[i][j] == 'T':
			s2mat[i][2]+=1
		if s2list[i][j] == 'C':
			s2mat[i][3]+=1
		if s2list[i][j] == 'G':
			s2mat[i][4]+=1

for i in range(len(s1mat)):
	nextMat.append()
	for j in range(len(s2mat)):
		nextMat.append([s1mat[i]+s2mat[i],s1mat[i][1]+s2mat[i][1],s1mat[i][2]+s2mat[i][2],s1mat[i][3]+s2mat[i][3],s1mat[i][4]+s2mat[i][4]])

print(nextMat)