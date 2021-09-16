# http://rosalind.info/problems/grph/
with open('datasets/rosalind_grph.txt') as f:
    k = 3
    sequences = {}
    results = []

    buf = f.readline().rstrip()
    while buf:
        seq_id, seq = buf[1:], ''
        buf = f.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq += buf
            buf = f.readline().rstrip()
        sequences[seq_id] = seq

    for id1, seq1 in sequences.items():
        for id2, seq2, in sequences.items():
            if id1 != id2 and seq1.endswith(seq2[:k]):
                results.append((id1, id2))

    print('\n'.join(' '.join(ids) for ids in results))
