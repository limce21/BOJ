import sys


def lotto(S, isused, k, lst):
    global cnt
    if len(lst) == 6:
        print(lst)
    for i in range(k):
        if isused[i]:
            continue
        else:
            isused[i] = 1
            lst.append(S[i])
            lotto(isused, i)
            isused[i] = 0


while(1):
    inputt = list(map(int, sys.stdin.readline().split()))
    if inputt[0] == 0:
        break
    k = inputt[0]
    S = input[1:]
    cnt = 0
    isused = [0] * k
    lst = []
    lotto(S, isused, 1, lst)
