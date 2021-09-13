# http://rosalind.info/problems/revc/
from string import maketrans

with open('datasets/rosalind_revc.txt') as f:
    print(f.read()[::-1].translate(maketrans('ACGT', 'TGCA')))
