# http://rosalind.info/problems/cons/
from collections import Counter

with open('datasets/rosalind_cons.txt') as f:
    strings = []

    buf = f.readline().rstrip()
    while buf:
        seq_id, seq = buf[1:], ''
        buf = f.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq += buf
            buf = f.readline().rstrip()
        strings.append(seq)

    counters = map(Counter, zip(*strings))
    consensus = ''.join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = '\n'.join(b + ': ' + ' '.join(str(c[b]) for c in counters) for b in 'ACGT')
    print(consensus + '\n' + profile_matrix)
