import sys
import math
M, N = map(int, sys.stdin.readline().split())


def isPrime(num):
    i = 2
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


if M == 1 and N == 2:
    print(2)
else:
    for i in range(M, N+1):
        if i == 1:
            continue
        if isPrime(i):
            print(i)
