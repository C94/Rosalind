# http://rosalind.info/problems/subs/
with open('datasets/rosalind_subs.txt') as f:
    s, t = f.read().split()

    locations = []

    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            locations.append(i+1)

    print(' '.join(map(str, locations)))
