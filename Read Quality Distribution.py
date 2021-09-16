# http://rosalind.info/problems/phre/
from Bio import SeqIO

with open('datasets/rosalind_phre.txt') as f:
    threshold = float(f.readline())
    fastq_entries = SeqIO.parse(f, 'fastq')

    res = sum(x < threshold for x in
              list(sum(entry.letter_annotations['phred_quality']) / len(entry.letter_annotations['phred_quality'])
                   for entry in fastq_entries))
    print(res)
