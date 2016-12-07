# Calculates the amount of different 37-digit subsequences on a .fasta sequence

sequence = open('/mnt/Data/Documents/sequence.fasta','r').read().replace('\n', '')
list37DigitWords = {}
i=0
with open("e1-1c_output.txt", "w") as text_file:
	while i < len(sequence)-37:
		possible37DigitWord = sequence[i:i+37]
		if possible37DigitWord in list37DigitWords:
			list37DigitWords[possible37DigitWord]+=1
			text_file.write('\nThe subsequence %s occours %s times.' % (possible37DigitWord,list37DigitWords[possible37DigitWord]))
		else:
			list37DigitWords[possible37DigitWord] = 1
		i+=1

#with open("e1-1c_output.txt", "w") as text_file:
#	for word, amount in list37DigitWords.items():
#		text_file.write('\nThe subsequence %s occours %s times.' % (word,amount))