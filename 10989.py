import sys

N = int(sys.stdin.readline())
num_arr = [0] * 10001

for i in range(N):
    num_arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_arr[i] != 0:
        for j in range(num_arr[i]):
            print(i)
