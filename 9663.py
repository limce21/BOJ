import sys
N = int(sys.stdin.readline())

cnt = 0
row = [0] * N


def isfind(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def func(x):
    if x == N:
        global cnt
        cnt += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if isfind(x):
                func(x+1)


func(0)
print(cnt)
