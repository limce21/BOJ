import sys
N, M = map(int, sys.stdin.readline().split())
a_arr = []
b_arr = []
for i in range(N):
    a_arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    b_arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        print(a_arr[i][j] + b_arr[i][j], end=' ')
    print()
