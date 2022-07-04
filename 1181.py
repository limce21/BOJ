import sys
N = int(sys.stdin.readline())

list_N = []
for i in range(N):
    list_N.append(sys.stdin.readline().strip())

list_N = list(set(list_N))
list_N.sort(key=lambda x: (len(x), x))

for i in list_N:
    print(i)
