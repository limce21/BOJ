import sys
N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))


def isIn(lst, idx, start, end):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == M_list[idx]:
            return True
        elif lst[mid] > M_list[idx]:
            end = mid - 1
        else:
            start = mid + 1


for i in range(M):
    if isIn(N_list, i, 0, N-1):
        print(1)
    else:
        print(0)
