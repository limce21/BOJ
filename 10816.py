import sys
N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = sorted(list(map(int, sys.stdin.readline().split)))


def isIn(a, x, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            end = mid - 1
        else:
            start = mid + 1


for i in range(M):
    if isIn(N_list, M_list[i], 0, M-1):
       
