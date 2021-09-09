# http://rosalind.info/problems/dna/
with open('datasets/rosalind_dna.txt') as f:
    molecule_count = {}
    for molecule in f.read():
        molecule_count[molecule] = molecule_count.get(molecule, 0) + 1

    print molecule_count['A'], molecule_count['C'], molecule_count['G'], molecule_count['T']

    f.close()
