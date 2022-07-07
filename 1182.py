from itertools import combinations
import sys

N, S = map(int, sys.stdin.readline().split())
cnt = 0
int_lst = list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    lst = list(combinations(int_lst, i))
    for j in lst:
        if sum(j) == S:
            cnt += 1

print(cnt)
