# http://rosalind.info/problems/fib/
def fib(n, k):
    if n <= 1:
        return n
    return fib(n - 1, k) + k * fib(n - 2, k)


with open('datasets/rosalind_fib.txt') as f:
    n, k = f.readline().split()
    res = fib(int(n), int(k))
    print(res)

    f.close()
