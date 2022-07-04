import sys
N = int(sys.stdin.readline())
list_N = list(map(int, sys.stdin.readline().split()))

list_N = list(set(list_N))
list_N.sort()

for i in list_N:
    print(i, end=' ')
