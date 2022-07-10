import sys
N = int(sys.stdin.readline())
prime_list = list(map(int, sys.stdin.readline().split()))

prime_cnt = 0

for i in prime_list:
    divisor_num = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisor_num += 1
    if divisor_num == 2:
        prime_cnt += 1
print(prime_cnt)
