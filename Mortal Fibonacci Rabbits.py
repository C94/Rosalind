# http://rosalind.info/problems/fibd/
with open('datasets/rosalind_fibd.txt') as f:
    n, m = map(int, f.readline().split())
    ages = [1] + [0] * (m - 1)

    for i in xrange(n - 1):
        ages = [sum(ages[1:])] + ages[:-1]

    print(sum(ages))
