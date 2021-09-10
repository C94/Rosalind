# http://rosalind.info/problems/rna/
with open('datasets/rosalind_rna.txt') as f:
    print(f.read().replace('T', 'U'))

    f.close()
