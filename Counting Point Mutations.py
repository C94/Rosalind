# http://rosalind.info/problems/hamm/
import operator

with open('datasets/rosalind_hamm.txt') as f:
    s, t = f.readlines()
    print(sum(map(operator.ne, s, t)))

    f.close()
