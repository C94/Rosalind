# http://rosalind.info/problems/gc/
with open('datasets/rosalind_gc.txt') as f:
    max_gc_id, max_gc = '', 0.0

    buf = f.readline().rstrip()
    while buf:
        seq_id, seq = buf[1:], ''
        buf = f.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq += buf
            buf = f.readline().rstrip()
        seq_gc = (seq.count('C') + seq.count('G')) / float(len(seq))
        if seq_gc > max_gc:
            max_gc_id, max_gc = seq_id, seq_gc

    print('%s\n%f' % (max_gc_id, max_gc * 100))
