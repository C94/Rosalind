# http://rosalind.info/problems/tfsq/
from Bio import SeqIO

with open('datasets/rosalind_tfsq.txt') as input_data, open('output.txt', 'w') as output_data:
    SeqIO.convert(input_data, 'fastq', output_data, 'fasta')
