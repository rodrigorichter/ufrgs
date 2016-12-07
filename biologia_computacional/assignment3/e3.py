# Read a DNA Sequence
def readSequence():
	sequence = open(raw_input('Enter sequence filename: '),'r')
	sequence.readline()
	sequence = sequence.read().replace('\n', '')
	return sequence

def match(a, b):
	if a == b:
		return 1
	else:
		return -1

# Align two sequences using Smith-Waterman algorithm
def alignSequences(s1, s2):
	gap = -2

	s1 = '-'+s1
	s2 = '-'+s2

	mWidth = len(s1)
	mHeight = len(s2)
	similarity_matrix = [[i for i in xrange(mHeight)] for i in xrange(mWidth)]

	for i in range (mWidth):
		similarity_matrix[i][0] = 0
		
	for j in range (mHeight):
		similarity_matrix[0][j] = 0
		
	for i in range (1,mWidth):
		for j in range (1, mHeight):
			p0 = 0
			p1 = similarity_matrix[i-1][j-1] + match(s1[i], s2[j])
			p2 = similarity_matrix[i][j-1] + gap
			p3 = similarity_matrix[i-1][j] + gap
			similarity_matrix[i][j] = max(p0, p1, p2, p3)

	#Find biggest number in the similarity matrix
	maxNumber = 0
	maxNumberI = 0
	maxNumberJ = 0
	for i in range(mWidth):
		for j in range(mHeight):
			if similarity_matrix[i][j] >= maxNumber:
				maxNumber = similarity_matrix[i][j]
				maxNumberI = i
				maxNumberJ = j

	i = maxNumberI
	j = maxNumberJ
	alignmentS1 = ''
	alignmentS2 = ''
	while similarity_matrix[i][j] > 0:
		if similarity_matrix[i][j] == similarity_matrix[i-1][j-1] + match(s1[i], s2[j]):
			alignmentS1 = s1[i] + alignmentS1
			alignmentS2 = s2[j] + alignmentS2
			j-=1
			i-=1
		elif similarity_matrix[i][j] == similarity_matrix[i-1][j] + gap:
			alignmentS1 = s1[i] + alignmentS1
			alignmentS2 = '-' + alignmentS2
			i-=1
		else:
			alignmentS1 = '-' + alignmentS1
			alignmentS2 = s2[j] + alignmentS2
			j-=1

	qtdeAlinhamento = 0
	for i in range(max(len(alignmentS1), len(alignmentS2))):
		if alignmentS1[i] == alignmentS2[i]:
			qtdeAlinhamento+=1
	print('Tabela final:',similarity_matrix)
	print('Melhor alinhamento local para a sequencia 1: ', alignmentS1)
	print('Melhor alinhamento local para a sequencia 2: ', alignmentS2)
	print('Identidade do alinhamento: ', qtdeAlinhamento)



s1 = readSequence()
s2 = readSequence()
alignSequences(s1, s2)