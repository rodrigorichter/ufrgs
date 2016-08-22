# Calculates the amount of different 37-digit subsequences on a .fasta sequence

sequence = open('/mnt/Data/Documents/sequence.fasta','r').read().replace('\n', '')
list37DigitWords = {}
i=0

while i < len(sequence)-37:
	possible37DigitWord = sequence[i:i+37]
	if possible37DigitWord in list37DigitWords:
		list37DigitWords[possible37DigitWord]+=1
	else:
		list37DigitWords[possible37DigitWord] = 1
	i+=1

for word, amount in list37DigitWords.items():
	print('The subsequence '+word+' occours '+str(amount)+' times.')