import sys
N = int(sys.stdin.readline())

list_N = []
for i in range(N):
    list_N.append(list(map(int, sys.stdin.readline().split())))

list_N.sort(key=lambda x: (x[1], x[0]))

for i in list_N:
    print(i[0], i[1])
