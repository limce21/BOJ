import sys
T = int(sys.stdin.readline())


def merg(value, sum):
    global result
    if sum >= n:
        return
    sum += value
    if sum == n:
        result += 1
    merg(1, sum)
    merg(2, sum)
    merg(3, sum)


for _ in range(T):
    n = int(sys.stdin.readline())
    result = 0
    merg(0, 0)
    print(result)
