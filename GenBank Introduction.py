# http://rosalind.info/problems/gbk/
from Bio import Entrez

with open('datasets/rosalind_gbk.txt') as f:
    genus, start, end = f.read().split()
    searchTerm = f'{genus}[Organism] AND ("{start}"[Publication Date] : "{end}"[Publication Date])'

    Entrez.email = '<insert email address here>'
    handle = Entrez.esearch("nucleotide", searchTerm)
    record = Entrez.read(handle)

    handle.close()

    print(record['Count'])
