sequence = open('sequence.fasta','r')

subseq = [2,1,1,0,0,3,1,1,0,1,1,0,0,3]
listpossiblemutations = []
listpossiblemutations.append(list(subseq))

# generate list of possible mutations for subsequence
for i, bit in enumerate(subseq):
	possibleseq = list(subseq)
	for j in range(0, 4):
		if j != bit:
			possibleseq[i] = j
			listpossiblemutations.append(list(possibleseq))

# transform possible sequences to tacg format
for i in range(len(listpossiblemutations)):
	for j in range(len(listpossiblemutations[i])):
		if listpossiblemutations[i][j] == 0:
			listpossiblemutations[i][j] = 'T'
		elif listpossiblemutations[i][j] == 1:
			listpossiblemutations[i][j] = 'A'
		elif listpossiblemutations[i][j] == 2:
			listpossiblemutations[i][j] = 'C'
		elif listpossiblemutations[i][j] == 3:
			listpossiblemutations[i][j] = 'G'
	listpossiblemutations[i] = ''.join(listpossiblemutations[i])

matches = open('matches.txt', 'w')

# try to find each of the sequences in the file
for line in sequence:
	for i in range(len(listpossiblemutations)):
		if line.find(listpossiblemutations[i]) > -1:
			matches.write(listpossiblemutations[i]+'\n')

matches.close()

