# Calculates the amount of 9-digit palindromes on a .fasta sequence

sequence = open('/mnt/Data/Documents/sequence.fasta','r').read().replace('\n', '')
listPalindromeWords = {}

i=0
while i < len(sequence)-9:
	possiblePalindromeWord = sequence[i:i+9]
	if possiblePalindromeWord == ''.join(reversed(possiblePalindromeWord)):
		if possiblePalindromeWord in listPalindromeWords:
			listPalindromeWords[possiblePalindromeWord]+=1
		else:
			listPalindromeWords[possiblePalindromeWord] = 1
	i+=1

totalAmountOfPalindromes=0
with open("e1-1b_output.txt", "w") as text_file:
	for word, amount in listPalindromeWords.items():
		text_file.write("\nThe palindrome subsequence %s occurs %s" % (word, amount))
		totalAmountOfPalindromes+=amount

	text_file.write('\nThe total amount of 9-digit palindrome subsequences found is %s.' % (totalAmountOfPalindromes))