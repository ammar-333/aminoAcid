readFile = input("Enter a file link for the dna sequance")

fo = open(readFile,'r')
dna = fo.read()

lines = dna.splitlines()
del lines[0]
dna = "\n".join(lines)

#transcribe the sequence to mRNA
mrna = dna.replace('T','U')

#translate the computed mRNA strand into amino acids
genetic_code = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
    'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP',
    'UAG': 'STOP', 'UGA': 'STOP'
}

codons = [mrna[i:i+3] for i in range(0, len(mrna), 3)]

amino_acids = []
for codon in codons:
    amino_acid = genetic_code.get(codon,"unknown")
    amino_acids.append(amino_acid)

amino_acid_sequence = " ".join(amino_acids)

print(amino_acid_sequence)
fo.close()
