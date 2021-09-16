# http://rosalind.info/problems/ini/
from Bio.Seq import Seq

with open('datasets/rosalind_ini.txt') as f:
    dna = Seq(f.readline())
    print(' '.join(map(str, (dna.count(c) for c in 'ACGT'))))
