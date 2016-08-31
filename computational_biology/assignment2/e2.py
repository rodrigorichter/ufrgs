# Read a DNA Sequence
def readSequence():
	sequence = open(raw_input('Enter sequence filename: '),'r').read().replace('\n', '')
	sequence = sequence[sequence.find('SEQUENCE')+8:]
	return sequence

def match(a, b):
	if a == b:
		return 5
	else:
		return -3

# Align two sequences using Needleman-Wunsch algorithm
def alignSequences(s1, s2):
	gap = -4

	matrixSize = max(len(s1), len(s2))
	similarity_matrix = [[0 for i in xrange(matrixSize)] for i in xrange(matrixSize)]


	for i in range (0,len(s1)):
		similarity_matrix[i][0] = gap*i
	for j in range (0,len(s2)):
		similarity_matrix[0][j] = gap*j
	for i in range (1,matrixSize):
		for j in range (1, matrixSize):
			p1 = similarity_matrix[i-1][j-1] + match(s1[i], s2[j])
			p2 = similarity_matrix[i][j-1] + gap
			p3 = similarity_matrix[i-1][j] + gap
			similarity_matrix[i][j] = max(p1, p2, p3)
	
	i = matrixSize-1
	j = matrixSize-1
	alignmentS1 = ''
	alignmentS2 = ''
	total = 0
	while i > 0 and j > 0:
		if i > 0 and j > 0 and similarity_matrix[i][j] == similarity_matrix[i-1][j-1] + match(s1[i], s2[j]):
			total+=similarity_matrix[i][j]
			alignmentS1 = s1[i] + alignmentS1
			alignmentS2 = s2[i] + alignmentS2
			j-=1
			i-=1
		elif j > 0 and similarity_matrix[i][j] == similarity_matrix[i-1][j] + gap:
			alignmentS1 = s1[i] + alignmentS1
			alignmentS2 = '-' + alignmentS2
			j-=1
		else:
			alignmentS1 = '-' + alignmentS1
			alignmentS2 = s2[i] + alignmentS2
			i-=1

	qtdeAlinhamento = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			qtdeAlinhamento+=1
	print('Tabela final:',similarity_matrix)
	print('Sequencia 1 alinhada: ', alignmentS1)
	print('Sequencia 2 alinhada: ', alignmentS2)
	print('Score do alinhamento: ', total)
	print('Identidade do alinhamento: ', qtdeAlinhamento)



s1 = readSequence()
s2 = readSequence()
alignSequences(s1, s2)