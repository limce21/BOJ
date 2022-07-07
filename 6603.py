from itertools import combinations
import sys

while(1):
    inputt = list(map(int, sys.stdin.readline().split()))
    if inputt[0] == 0:
        break
    k = inputt[0]
    S = inputt[1:]
    lst = list(combinations(S, 6))
    for i in lst:
        for j in range(6):
            print(i[j], end=" ")
        print()
    print()
