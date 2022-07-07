import sys
T = int(sys.stdin.readline())


def plus(x):
    if x == 0:
        return
    lst = [1] * x
    result = 1
    result += plus(x-1)
    return result


for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = plus(n)
    print(cnt)
