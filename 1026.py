import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = list(map(int, sys.stdin.readline().split()))

S = 0

for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))

print(S)
