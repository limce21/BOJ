import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

ans_dict = {}

for i in N_list:
    ans_dict[i] = 0

for i in M_list:
    ans_dict[i] = 0

for i in N_list:
    ans_dict[i] += 1

for i in M_list:
    print(ans_dict[i], end=" ")
