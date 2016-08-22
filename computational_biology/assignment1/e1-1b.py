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
for word, amount in listPalindromeWords.items():
	print('The palindrome subsequence '+word+' occours '+str(amount)+' times.')
	totalAmountOfPalindromes+=amount

print('The total amount of 9-digit palindrome subsequences found is '+str(totalAmountOfPalindromes)+'.')