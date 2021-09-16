# http://rosalind.info/problems/frmt/
from Bio import Entrez, SeqIO

with open('datasets/rosalind_frmt.txt') as f:
    genbank_ids = f.readline().split()

    Entrez.email = '<insert email address here>'
    handle = Entrez.efetch(db='nucleotide', id=genbank_ids, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))
    handle.close()

    print(min(records, key=lambda s: len(s.seq)).format('fasta'))
