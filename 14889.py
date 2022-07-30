import sys
N = int(sys.stdin.readline())
S_list = []
for i in N:
    S_list.append(list(map(int, sys.stdin.readline().split())))

print(S_list)
