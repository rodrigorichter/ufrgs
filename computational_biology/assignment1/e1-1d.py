# Calculates the amount of each nucleotide on a .fasta sequence

sequence = open('/mnt/Data/Documents/sequence.fasta','r').read().replace('\n', '')

nucleotides = {
	'A': 0,
	'T': 0,
	'C': 0,
	'G': 0
}

i=0
while i < len(sequence):
	if sequence[i] not in nucleotides:
		print('Wrong character found: '+sequence[i])
	else:
		nucleotides[sequence[i]]+=1
	i+=1

for nucleotide, amount in nucleotides.items():
	print("The nucleotide "+nucleotide+" occurs "+str(amount)+" times.")