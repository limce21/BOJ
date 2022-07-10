import sys
import math
M, N = map(int, sys.stdin.readline().split())


def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(M, N+1):
    if primality(i):
        print(i)
